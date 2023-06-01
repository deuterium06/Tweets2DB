CREATE DATABASE IF NOT EXISTS tweets;

use tweets;

CREATE TABLE IF NOT EXISTS twitter_raw (
    pk int(11) AUTO_INCREMENT PRIMARY KEY,

    -- Tweets
    tweet_id bigint,
    tweet_content longtext DEFAULT NULL,
    tweet_url varchar(255) DEFAULT NULL,
    tweet_source varchar(255) DEFAULT NULL,
    tweet_language varchar(50) DEFAULT NULL,
    tweet_date timestamp NULL,
    tweet_reply_count int,
    tweet_retweet_count int,
    tweet_like_count int,
    tweet_quote_count int,
    
    -- Users
    user_id bigint,
    username varchar(50) DEFAULT NULL,
    user_displayname varchar(50) DEFAULT NULL,
    user_description longtext DEFAULT NULL,
    user_location varchar(50) DEFAULT NULL,
    user_created timestamp NULL,
    user_followers_count int,
    user_friends_count int,
    user_statuses_count int,

    date_added timestamp DEFAULT CURRENT_TIMESTAMP,
    date_updated timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);