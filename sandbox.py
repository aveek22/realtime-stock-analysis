import json

tweet_response = {
    "tweet_id": "1419492195355201537",
    "hashtags": [
        {
            "text": "Vacunas",
            "indices": [
                21,
                29
            ]
        },
        {
            "text": "Covid19",
            "indices": [
                30,
                38
            ]
        },
        {
            "text": "Corrientes",
            "indices": [
                102,
                113
            ]
        }
    ]
}

print(type(tweet_response))

print(tweet_response['hashtags'][1]['text'])

list_hashtags = []

for hashtag in tweet_response['hashtags']:
    dict_hashtag = {
        'tweet_id' : tweet_response['tweet_id'],
        'hashtag' : hashtag['text']
    }
    # print(dict_hashtag)
    list_hashtags.append(dict_hashtag)

list_hashtags_str = json.dumps(list_hashtags)

print(type(list_hashtags_str))