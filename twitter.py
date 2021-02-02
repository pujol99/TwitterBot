import tweepy as tp
from credentials import *

# credentials to login to twitter api
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_secret = ACCESS_SECRET

class TwitterAPI:
    def __init__(self):
        auth = tp.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        self.api = tp.API(auth)

    def me(self):
        return self.api.me()

    def friends(self, id):
        return self.api.followers_ids(id)

    def most_popular(self, ids):
        popular = -1, None
        for id in ids:
            user = self.api.get_user(id)
            print(user.followers_count, user.name)
            # if len(self.api.followers(id)) > popular[0]:
            #     popular = self.api.followers(id), self.api.get_user(id)

        return popular[1]

twitter = TwitterAPI()
print(twitter.most_popular(twitter.friends(twitter.me().id)))