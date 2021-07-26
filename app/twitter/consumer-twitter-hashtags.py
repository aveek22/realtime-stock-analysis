from kafka import KafkaConsumer
import utils.database as db
import utils.util as ut
import json

def main():
    try:
        consumer = KafkaConsumer(
            'topic-twitter-hashtags',
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
                list_hashtags = message.value
                
                # Process message if not empty
                if(list_hashtags):
                    print(f'{list_hashtags}')
                    
                    for hashtag in list_hashtags:
                        tweet_id = hashtag['tweet_id']
                        hashtag_str = hashtag['hashtag']
                        lang = hashtag['lang']

                        db.insert_twitter_hashtags(tweet_id,hashtag_str,lang)
            except Exception as error:
                print(f'Error in reading message from the consumer. {error}')


if __name__ == '__main__':
    main()