CREATE DATABASE IF NOT EXISTS tweets;

use tweets;

CREATE TABLE IF NOT EXISTS tweet_facts (
    id int(11) PRIMARY KEY AUTO_INCREMENT,
    tweetid int(11),
    userid int(11),
    reply_count int,
    retweet_count int,
    like_count int,
    quote_count int,
    date_added timestamp DEFAULT CURRENT_TIMESTAMP,
    date_updated timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS tweets (
    -- Tweets
    id int(11) PRIMARY KEY AUTO_INCREMENT,
    tweetid_ bigint,
    content longtext DEFAULT NULL,
    `url` varchar(255) DEFAULT NULL,
    source varchar(255) DEFAULT NULL,
    `language` varchar(50) DEFAULT NULL,
    created timestamp NULL,
    date_added timestamp DEFAULT CURRENT_TIMESTAMP,
    date_updated timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT tweetid_unique UNIQUE (tweetid_)
);

CREATE TABLE IF NOT EXISTS users (
    -- Users
    id int(11) PRIMARY KEY AUTO_INCREMENT,
    userid_ bigint,
    username varchar(50) DEFAULT NULL,
    displayname varchar(50) DEFAULT NULL,
    `description` longtext DEFAULT NULL,
    `location` varchar(50) DEFAULT NULL,
    created timestamp NULL,
    followers_count int,
    friends_count int,
    statuses_count int,
    date_added timestamp DEFAULT CURRENT_TIMESTAMP,
    date_updated timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT userid_unique UNIQUE (userid_)
);
