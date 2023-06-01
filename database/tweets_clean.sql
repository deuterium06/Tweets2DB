CREATE DATABASE IF NOT EXISTS tweets;

use tweets;

CREATE TABLE IF NOT EXISTS tweet_facts (
    tweet_id bigint PRIMARY KEY,
    user_id bigint,
    reply_count int,
    retweet_count int,
    like_count int,
    quote_count int,
    date_added timestamp DEFAULT CURRENT_TIMESTAMP,
    date_updated timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


CREATE TABLE tweets (
    -- Tweets
    tweet_id bigint PRIMARY KEY,
    content longtext DEFAULT NULL,
    `url` varchar(255) DEFAULT NULL,
    source varchar(255) DEFAULT NULL,
    `language` varchar(50) DEFAULT NULL,
    created timestamp NULL,
    date_added timestamp DEFAULT CURRENT_TIMESTAMP,
    date_updated timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE users (
    -- Users
    user_id bigint PRIMARY KEY,
    username varchar(50) DEFAULT NULL,
    displayname varchar(50) DEFAULT NULL,
    `description` longtext DEFAULT NULL,
    `location` varchar(50) DEFAULT NULL,
    created timestamp NULL,
    followers_count int,
    friends_count int,
    statuses_count int,
    date_added timestamp DEFAULT CURRENT_TIMESTAMP,
    date_updated timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
