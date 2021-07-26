from kafka import KafkaConsumer
import utils.database as db
import utils.util as ut
import json

def main():
    try:
        consumer = KafkaConsumer(
            'topic-twitter-response',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
    except Exception as error:
        print(f'Error in initialising the consumer. {error}')
        consumer = False


    if(consumer):
        for message in consumer:
            try:
                message = message.value
                print(f'{message}')

                tweet_dttm, = message['tweet_dttm'],
                tweet_id, = message['tweet_id'],
                tweet_text, = message['tweet_text'],
                source, = message['source'],
                user_screen_name, = message['user_screen_name'],
                geo, = message['geo'],
                coordinates, = message['coordinates'],
                # place, = message['place'],
                contributors, = message['contributors'],
                retweet_count, = message['retweet_count'],
                favorite_count, = message['favorite_count'],
                is_retweet, = message['is_retweet'],
                # is_sensitive = message['is_sensitive'],
                lang = message['lang']

                db.insert_twitter_stream(tweet_dttm,tweet_id,tweet_text,source,user_screen_name,geo,coordinates,contributors,retweet_count,favorite_count,is_retweet,lang)
            except Exception as error:
                print(f'Error in reading message from the consumer. {error}')


if __name__ == '__main__':
    main()