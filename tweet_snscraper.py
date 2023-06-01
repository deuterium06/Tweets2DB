
import snscrape.modules.twitter as sntwitter
import pandas as pd

from tweet_db import TweetDb
from utils.constants import PROJECT_ROOT
from utils.mysql_db import MySQLDB

TWEET_LIMIT = 2;

class TweetSnscraper:
    
    def __init__(self):
        self.db = TweetDb()

    def scrape(self, query='sample'):

        '''
        format:
            tweets = [
                {'tweetid':1,'content':'ABC',...},
                {'tweetid':2,'content':'XYZ',...}
            ]

            values = [
                [1,'ABC',...],
                [2,'XYZ',...]
            ]        
        '''
        tweets = list()
        values = list()
        db = self.db

        for tweet in sntwitter.TwitterSearchScraper(query).get_items():

            if len(tweets) > TWEET_LIMIT:
                
                break;

            else:
                
                ### Tweets
                tweet_dict = dict()

                tweet_dict['tweet_id'] = tweet.id,
                tweet_dict['tweet_content'] = tweet.rawContent,
                tweet_dict['tweet_url'] = tweet.url,
                tweet_dict['tweet_source'] = tweet.source,
                tweet_dict['tweet_language'] = tweet.lang,
                tweet_dict['tweet_date'] = tweet.date,
                tweet_dict['tweet_reply_count'] = tweet.replyCount,
                tweet_dict['tweet_retweet_count'] = tweet.retweetCount,
                tweet_dict['tweet_like_count'] = tweet.likeCount,
                tweet_dict['tweet_quote_count'] = tweet.quoteCount
               
                ### Users
                tweet_dict['user_id'] = tweet.user.id,
                tweet_dict['username'] = tweet.user.username,
                tweet_dict['user_displayname'] = tweet.user.displayname,
                tweet_dict['user_description'] = tweet.user.renderedDescription,
                tweet_dict['user_location'] = tweet.user.location,
                tweet_dict['user_created'] = tweet.user.created
                tweet_dict['user_followers_count'] = tweet.user.followersCount,
                tweet_dict['user_friends_count'] = tweet.user.friendsCount,
                tweet_dict['user_statuses_count'] = tweet.user.statusesCount

                tweets.append(tweet_dict)
                
                value = [i for i in tweet_dict.values()]
                values.append(value)
        
        try:
            print('Scrape has been successful. Now, inserting data into db...')
            db.insert_table(table='twitter_raw',values=values)
            db.quit()
            print('Data has been successfully loaded into database.')
            #print(tweets)
        
        except Exception as e:
            self.save_to_csv(tweets)
            print('Oppps! There is an issue while inserting data into db. Data is stored in a local CSV file instead.')

            db.rollback()
            print(f"Error: {e}")

    def check_query(self):
        return None

    def save_to_csv(self, dict_list:list):

        tweet_df = pd.DataFrame(dict_list)
        tweet_df.to_csv(PROJECT_ROOT + r"\tweets_raw.csv", float_format='%g')

    
    def get_tweets_results(self, query):

        try:
            self.scrape(query)
        except Exception as e:
            print('Something went wrong while trying to scrape: ' + str(e))

if __name__ == '__main__':
    
    '''
    Scrape tweet query & save data to Local DB
    '''

    tweet_scraper = TweetSnscraper()
    tweet_scraper.get_tweets_results("Pokemon")