import numpy as np
import datetime
from pytz import timezone
import database as db
import time
import json

def generate_dummy_data(symbol):

    if(symbol == 'AAPL'):
        close = 147.31
    elif(symbol == 'MSFT'):
        close = 285.35
    elif(symbol == 'GOOGL'):
        close = 2561.02
    elif(symbol == 'FB'):
        close = 350.2
    elif(symbol == 'AMZN'):
        close = 3620.02


    try:
        # Generate dummy stock data
        close = round(close+np.random.uniform(-200,200),5)
        message = {'T':"b",
                'S':symbol,
                'o':round(close+np.random.uniform(-1,1),5),
                'c':close,
                'h':round(close+np.random.uniform(0,1),5),
                'l':round(close+np.random.uniform(-1,0),5),
                't':str(datetime.datetime.now()),
                'v':round(np.random.uniform(0,1)*6e2,0),
                'vw':close,}
    except Exception as error:
        print(f'Error creating dummy stock data. {error}')
    
    try:
        # Print and write data
        message_json = json.dumps(message)
        print(f'Dummy stock data: {message_json}')
        # Insert data to the database
        write_to_db(message)
    except Exception as error:
        print(f'Error converting dummy stock data to string. {error}')

def write_to_db(message):

    try:
        message_type, = message['T'],
        symbol, = message['S'],
        open_price, = message['o'],
        high_price, = message['h'],
        low_price, = message['l'],
        close_price, = message['c'],
        volume, = message['v'],
        traded_dttm_utc_str = message['t']
    except Exception as error:
        print(f'Error extracting message details. {error}')

    db.insert_stock_data(message_type,symbol,open_price,high_price,low_price,close_price,volume,traded_dttm_utc_str)


def main():
    while(True):
        generate_dummy_data('AAPL')
        generate_dummy_data('MSFT')
        time.sleep(1)

if __name__ == '__main__':
    main()