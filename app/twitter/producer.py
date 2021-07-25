'''
    This is the producer file that streams the tweets from the Twitter Streaming API into Kafka
'''

import utils.config as config
import tweepy
from kafka import KafkaProducer
import json
import os

# Fetch the credentials
TWITTER_API_KEY             = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET          = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN        = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Create the authentication object
try:
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

    # Create the API object
    api = tweepy.API(auth)
except Exception as error:
    print(f'Error in authentication. {error}')

class MyStreamListener(tweepy.StreamListener):

    def __init__(self):
        try:
            self.api = api
            super(tweepy.StreamListener, self).__init__()
            self.producer = KafkaProducer()
        except Exception as error:
            print(f'Error initiating Kafka Producer. {error}')
                          
    def on_status(self, status):
        
        # Extract the tweet response from the tweet status
        tweet_response_str = self.extract_status(status)
        
        # Send messages to the Kafka topic
        try:
            self.producer.send('my_first_topic', tweet_response_str.encode('utf-8'))
        except Exception as error:
            print(f'Error sending data to Kafka topic. {error}')

    def extract_status(self,status):
        try:
            tweet_dttm          = status.created_at
            tweet_id            = status.id_str
            tweet_text          = status.text.encode('utf-8')
            entities            = status.entities
            source              = status.source
            user_screen_name    = status.user.screen_name
            geo                 = status.geo
            coordinates         = status.coordinates
            # place               = status.place
            contributors        = status.contributors
            retweet_count       = status.retweet_count
            favorite_count      = status.favorite_count
            is_retweet          = status.retweeted
            # is_sensitive        = status.possibly_sensitive
            lang                = status.lang
        except Exception as error:
            print(f'Error extracting status. {error}')
            # print(f'TweetID: {tweet_id} with text: {tweet_text} at {tweet_dttm}')

        
        try:
            tweet_response = {
                'tweet_dttm' : tweet_dttm.isoformat(),
                'tweet_id' : tweet_id,
                'tweet_text' : tweet_text.decode('UTF-8'),
                'hashtags' : entities['hashtags'],
                'source' : source,
                'user_screen_name' : user_screen_name,
                'geo' : geo,
                'coordinates' : coordinates,
                # 'place' : place,
                'contributors' : contributors,
                'retweet_count' : retweet_count,
                'favorite_count' : favorite_count,
                'is_retweet' : is_retweet,
                # 'is_sensitive' : is_sensitive,
                'lang' : lang
            }
        except Exception as error:
            print(f'Error preparing tweet_repsponse from status. {error}')

        try:
            tweet_response_str = json.dumps(tweet_response)
            print(f'Tweet Response: {tweet_response_str}')
        except Exception as error:
            print(f'Error converting tweet response as JSON. {error}')
            tweet_response_str = False

        return tweet_response_str

def main():
    
    try:
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
        myStream.filter(track=['Covid19'])
        # myStream.filter(follow=["168206079"])
    except Exception as error:
        print(f'Error fetching streaming data. {error}')


if __name__ == '__main__':
    main()