CREATE TABLE twitter_hashtags(
    id                  serial,
    tweet_id            varchar(50),
    hashtag             varchar(50),
    lang                varchar(20),
    created_dttm        timestamp 
);

ALTER TABLE twitter_hashtags ALTER COLUMN created_dttm SET DEFAULT now();