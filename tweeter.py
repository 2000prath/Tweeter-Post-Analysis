import tweepy
from textblob import TextBlob
import math
consumer_key = 'your key'
consumer_secret = 'secret_key'

access_token = 'your token'
access_token_secret = 'token_secret'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


def predict(text):
    api=tweepy.API(auth)
    #print(api.trends_place(id=1))
    public_tweets = api.search(str(text),lang='en',count="100")
    data=[]
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
    
        a=analysis.sentiment.polarity
        print(analysis.sentiment)
        result={}
        if(a==0):
            result["text"]=tweet.text
            result["sentiment"]=0
        if(a<0):
            result["text"]=tweet.text
            result["sentiment"]=-1
        if(a>0.0):
            result["text"]=tweet.text
            result["sentiment"]=1
        data.append(result)

    return data