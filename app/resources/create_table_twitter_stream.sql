CREATE TABLE twitter_stream_data(
    id                  serial,
    tweet_dttm          timestamp,
    tweet_id            varchar(50),
    tweet_text          text,
    source              varchar(20),
    user_screen_name    varchar(50),
    geo                 varchar(500),
    coordinates         varchar(500),
    place               varchar(50),
    contributors        varchar(50),
    retweet_count       int,
    favorite_count      int,
    is_retweet          boolean,
    is_sensitive        boolean,
    lang                varchar(20),
    created_dttm        timestamp 
);

ALTER TABLE twitter_stream_data ALTER COLUMN created_dttm SET DEFAULT now();


INSERT INTO twitter_stream_data (tweet_dttm,tweet_id,tweet_text,source,user_screen_name,geo,coordinates,place,contributors,retweet_count,favorite_count,is_retweet,is_sensitive,lang)
VALUES('2020-06-03 07:21:23','1268080321590935553','This is tweet text','Twitter Web App','geeksforgeeks',NULL,NULL,NULL,NULL,20,500,TRUE,FALSE,'en')