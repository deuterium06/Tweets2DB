import pandas as pd
from tweet_db import TweetDb

db = TweetDb()

# Extract data from the source
def extract_data():

    # check the last record from twitter_raw that was inserted into clean tables
    latest_tweetid = db.select_table(table='tweets', columns=['tweetid_'], latest=True, latest_id='id')

    if (latest_tweetid == []) or (latest_tweetid is None):
        last_pk = 0
    else:
        last_pk = db.select_table(table='twitter_raw', columns=['pk'], where='tweet_tweetid_ =' + str(latest_tweetid[0]), latest=True, latest_id='pk')[0]

    # get the names of columns from clean tables & modify to match with twitter_raw columns
    tweets_columns = db.select_column_names(table='tweets',  exclude_increment=True)
    tf_columns = db.select_column_names(table='tweet_facts',  exclude_increment=True) 
    users_columns = db.select_column_names(table='users',  exclude_increment=True)

    def append_to_each_list(value:str, column:list):
        new_column = []
        for i in column:
            i = value + i
            new_column.append(i)
        return new_column

    tweets_columns =  append_to_each_list('tweet_', tweets_columns)
    users_columns =  append_to_each_list('user_', users_columns)
    tf_columns = append_to_each_list('tweet_', tf_columns)

    tf_columns[0] = 'tweet_tweetid_'
    tf_columns[1] = 'user_userid_'

    # extract the data from twitter_raw from the last row (pk) that was ingested into clean tables
    raw_tweets_table = db.select_table(table='twitter_raw', columns=tweets_columns ,where='pk >' + str(last_pk))
    raw_tf_table = db.select_table(table='twitter_raw', columns=tf_columns ,where='pk >' + str(last_pk))
    raw_users_table = db.select_table(table='twitter_raw', columns=users_columns ,where='pk >' + str(last_pk))

    return raw_tweets_table, raw_users_table, raw_tf_table

# Transform & Load data into the destination
def transform_load_data(raw_tweets_table, raw_users_table, raw_tf_table):

    ### tweets_table

    if len(raw_tweets_table) > 0:
        
        db.insert_table(table='tweets', values=raw_tweets_table)
        print("ok")
    else:
        print("No new data found for tweets table. Skipping load process.")

    ### users_table

    if len(raw_users_table) > 0:
        
        userid_db =  db.select_table(table='users', columns=['userid_']) 
        user_columns = db.select_column_names(table='users',  exclude_increment=True)

        user_values = []

        for row in raw_users_table:

            if row[0] in userid_db:
                
                #check if user is existing in users table

                old_row = db.select_table(table='users', columns=user_columns, where='userid_=' + str(row[0]), latest=True)[0]
                new_row = row

                def check_lists_equal(list1, list2):
                    if len(list1) != len(list2):
                        return False

                    for value1, value2 in zip(list1, list2):
                        if value1 != value2:
                            return False
                    return True

                if not check_lists_equal(old_row,new_row):
                    #db.update_table(table='users', columns=user_columns, values=new_row, where='userid_=' + str(row[0]))	
                    pass
            else:
                user_values.append(row)
    
        db.insert_table(table='users', values=user_values)

    else:
        print("No new data found for users table. Skipping load process.")

    ### tweet_facts table
    
    if len(raw_tf_table) > 0:

        tf_columns = db.select_column_names(table='tweet_facts',  exclude_increment=True)
        tweetid_db = db.select_table(table='tweet_facts', columns=['tweetid'])
        
        tweet_facts_values = []

        for row in raw_tf_table:	
            
            # change twitter_raw user_id & tweet_ids with existing ids on tweets & users
            value = []	
            tweet_id = db.select_table(table='tweets', columns=['id'], where='tweetid_=' + str(row[0]))[0]
            user_id = db.select_table(table='users', columns=['id'], where='userid_=' + str(row[1]))[0]
            
            value.extend([tweet_id, user_id])
            value.extend(row[2:])

            #check if tweet is existing in tweet_facts table
            if value[0] in tweetid_db:    
                old_row = db.select_table(table='tweet_facts', columns=tf_columns, where='tweetid=' + str(value[0]))[0]
                new_row = row

                if not check_lists_equal(old_row,new_row):
                    #db.update_table(table='tweet_facts', columns=tf_columns, values=new_row, where='tweetid=' + str(value[0]))	
                    pass
            else:		        
                tweet_facts_values.append(value)

        db.insert_table(table='tweet_facts', values=tweet_facts_values)
    
    else:
        print("No new data found for tweet_facts table. Skipping load process.")

# Main ETL function
def etl_process():
    # Extract data from the source
    raw_tweets_table, raw_users_table, raw_tf_table = extract_data()

    # Load & transform raw data into the destination
    transform_load_data(raw_tweets_table, raw_users_table, raw_tf_table)

# Execute the ETL process
etl_process()
