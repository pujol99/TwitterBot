import tweepy as tp
from credentials import *

# credentials to login to twitter api
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_secret = ACCESS_SECRET

class TwitterAPI:
    self.api = None

    def __init__(self):
        auth = tp.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self.api = tp.API(auth)

    
