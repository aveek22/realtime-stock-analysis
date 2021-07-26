import psycopg2 as pg
import os
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


def insert_twitter_stream(tweet_dttm,tweet_id,tweet_text,source,user_screen_name,geo,coordinates,contributors,retweet_count,favorite_count,is_retweet,lang):
    '''
        This method will insert a record into the registered_users table.
    '''

    tweet_text = tweet_text.replace("'","''")

    # Create the connection object and run the stored procedure.
    connection = connect_database()
    if(connection):
        try:
            cursor = connection.cursor()
            logging.info(f'Calling stored procedure public.usp_insert_registered_users...')
            sql = f'INSERT INTO twitter_stream_data(tweet_dttm,tweet_id,tweet_text,source,user_screen_name,geo,coordinates,contributors,retweet_count,favorite_count,is_retweet,lang) VALUES (\'{tweet_dttm}\',\'{tweet_id}\',\'{tweet_text}\',\'{source}\',\'{user_screen_name}\',\'{geo}\',\'{coordinates}\',\'{contributors}\',{retweet_count},{favorite_count},{is_retweet},\'{lang}\');'
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

def insert_twitter_hashtags(tweet_id,hashtag,lang):
    '''
        This method will insert a record into the registered_users table.
    '''

    # Create the connection object and run the stored procedure.
    connection = connect_database()
    if(connection):
        try:
            cursor = connection.cursor()
            logging.info(f'Calling stored procedure public.usp_insert_registered_users...')
            sql = f'INSERT INTO twitter_hashtags(tweet_id,hashtag,lang) VALUES (\'{tweet_id}\',\'{hashtag}\',\'{lang}\');'
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
    # insert_twitter_stream('2020-06-03 07:21:23','1268080321590935553','This is tweet text','Twitter Web App','geeksforgeeks',None,None,None,None,20,500,True,False,'en')
    insert_twitter_hashtags('1268080321590935553','TestHashtag')

if __name__ == '__main__':
    main()