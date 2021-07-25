import psycopg2 as pg
# import os
import logging

DATABASE_HOSTNAME   = 'localhost'
DATABASE_USERNAME   = 'enviso'
DATABASE_PASSWORD   = 'test1234'

def connect_database():
    '''
        This method is used to connect to a postgresql database and return the
        connection object.
    '''
    try:
        logging.info('Connecting to database...')
        connection = pg.connect(
            host        = DATABASE_HOSTNAME,
            database    = 'stock_price_analysis',
            user        = DATABASE_USERNAME,
            password    = DATABASE_PASSWORD
        )
        logging.info('Database connected.')
        return connection
    except Exception as error:
        logging.error(f'Unable to connect to the database. Error: {error}')
        return False


def insert_stock_data(message_type,symbol,open_price,high_price,low_price,close_price,volume,traded_dttm_utc_str):
    '''
        This method will insert a record into the registered_users table.
    '''

    # Create the connection object and run the stored procedure.
    connection = connect_database()
    if(connection):
        try:
            cursor = connection.cursor()
            logging.info(f'Calling stored procedure public.usp_insert_registered_users...')
            sql = f'INSERT INTO stock_data(message_type,symbol,open_price,high_price,low_price,close_price,volume,traded_dttm_utc_str,traded_dttm_utc) VALUES (\'{message_type}\',\'{symbol}\',{open_price},{high_price},{low_price},{close_price},{volume},\'{traded_dttm_utc_str}\',\'{traded_dttm_utc_str}\');'
            cursor.execute(sql)
            connection.commit()
            # logging.info(f'User: {username} for Tenant: {tenantId} populated in the registered_users table.')
        except Exception as error:
            logging.error(f'Cannot insert record to database. Error: {error}')
            return False
        finally:
            cursor.close()
            connection.close()
    else:
        logging.warning(f'No connection to the database available.')
        return False


def main():
    insert_stock_data('bar','AAPL',145.345,145.32,145.65,145.20,345,'2021-07-21T18:01:00Z',)

if __name__ == '__main__':
    main()