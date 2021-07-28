from nltk.corpus import twitter_samples


# Creating variables to store the twitter sample files
tweet_positive = twitter_samples.strings('positive_tweets.json')
tweet_negative = twitter_samples.strings('negative_tweets.json')
tweet_text = twitter_samples.strings('tweets.20150430-223406.json')

print(twitter_samples.fileids())