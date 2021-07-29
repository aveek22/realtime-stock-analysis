from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re, string
import pickle

try:
    file_path = '/Users/aveek/Codebase/masters-thesis/realtime-stock-analysis/app/twitter/utils'
    f = open(f'{file_path}/my_classifier', 'rb')
    classifier_pickle = pickle.load(f)
    f.close()
except Exception as error:
    print(f'Error in loading model. {error}')

def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    try:
        for token, tag in pos_tag(tweet_tokens):
            token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                        '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
            token = re.sub("(@[A-Za-z0-9_]+)","", token)

            if tag.startswith("NN"):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'

            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token, pos)

            if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
                cleaned_tokens.append(token.lower())
    except Exception as error:
        print(f'Error in removing noise. {error}')
        cleaned_tokens = False
    
    return cleaned_tokens

def get_tweet_sentiment(custom_tweet):

    try:
        custom_tokens = remove_noise(word_tokenize(custom_tweet))
        sentiment = classifier_pickle.classify(dict([token, True] for token in custom_tokens))
    except Exception as error:
        print(f'Error in getting sentiment. {error}')
        sentiment = False
    
    return sentiment

if __name__ == '__main__':
    custom_tweet = 'I am happy with you.'
    print(get_tweet_sentiment(custom_tweet))