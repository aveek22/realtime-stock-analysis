import websocket
import json
import database as db
import os

# Fetch the API credentials
API_KEY     = os.getenv('ALPACA_API_KEY')
SECRET_KEY  = os.getenv('ALPACA_SECRET_KEY')

# Function called when web socket connection is opened.
def on_open(ws):
    '''
        This method is called when the connection to the socket is opened for the first time.
    '''
    print(f'Connection to websocket opened.')

    try:
        # Prepare the authorization payload
        auth_data = {
            "action"    : "auth",
            "key"       : API_KEY,
            "secret"    : SECRET_KEY
        }
        # Authenticate the websocket connection with the credentials
        ws.send(json.dumps(auth_data))
    except Exception as error:
        print(f'An error occured while authenticating with Alpaca. {error}')

    try:
        # Subscribe to a ticker
        listen_message = {
            "action" : "subscribe",
            # "trades": ["AAPL"],
            # "quotes": ["AAPL"]#,
            "bars": ["AAPL","MSFT","GOOGL","FB"]
        }
        ws.send(json.dumps(listen_message))
    except Exception as error:
        print(f'An error occured while subscribing to the tickers. {error}')

# Function called when a message is received from the web socket.
def on_message(ws, message):
    '''
        This method is called when a message is received from the web socket as a response.
    '''
    is_message_parsed = False

    # Load the message received as a JSON string
    try:
        message_json = json.loads(message)
        message_json = message_json[0]
        print(f'Received message: {message_json}.')
        is_message_parsed = True
    except Exception as error:
        print(f'An error occured while parsing string as JSON. {error}')
        is_message_parsed = False

    # Write message to database when bar data is recieved.
    # Logic: message_type = bar
    if(is_message_parsed == True):
        if(message_json['T'] == 'b'):
            # Insert data to the database
            write_to_db(message_json)

def write_to_db(message):
    
    message_json = message

    message_type, = str(message_json['T']),
    symbol, = message_json['S'],
    open_price, = message_json['o'],
    high_price, = message_json['h'],
    low_price, = message_json['l'],
    close_price, = message_json['c'],
    volume, = message_json['v'],
    traded_dttm_utc_str = message_json['t']

    db.insert_stock_data(message_type,symbol,open_price,high_price,low_price,close_price,volume,traded_dttm_utc_str)


def main():
    # socket_url = 'wss://data.alpaca.markets/stream'
    socket_url = 'wss://stream.data.alpaca.markets/v2/iex'

    # Create the websocket application
    ws = websocket.WebSocketApp(
        socket_url, 
        on_open = on_open,
        on_message = on_message
    )
    ws.run_forever()

def test():
    message = '[{"T":"b","S":"AAPL","o":145.39,"c":145.37,"h":145.39,"l":145.37,"v":1200,"t":"2021-07-21T18:46:00Z","n":9,"vw":145.380833}]'
    write_to_db(message)

if __name__ == '__main__':
    main()
    # test()
