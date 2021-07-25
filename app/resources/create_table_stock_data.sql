CREATE TABLE stock_data(
    stock_data_id       serial,
    message_type        varchar(20),
    symbol              varchar(20),
    open_price          decimal(9,4),
    high_price          decimal(9,4),
    low_price           decimal(9,4),
    close_price         decimal(9,4),
    volume              integer,
    traded_dttm_utc_str varchar(50),
    traded_dttm_utc     timestamp,
    traded_dttm_est     timestamp
);

INSERT INTO stock_data(message_type,symbol,open_price,high_price,low_price,close_price,volume,traded_dttm_utc_str,traded_dttm_utc)
VALUES ('b','AAPL',145.345,145.32,145.65,145.20,345,'2021-07-21T18:01:00Z','2021-07-21T18:01:00Z');