import tweepy
import botometer
import json
import time

consumer_key = "TyIlP6mnNgQgGSmuuqGZ77SeP"
consumer_secret = "KLJUO4ZssEt06GkPz1r74FA8p2FmyK0LK23pwQHSOJm5k9PpPy"
access_token_key = "2830897771-VRxmf5eYXxCcsRwjdMhmAxO89pIrBttYM5H5gx9"
access_token_secret = "DfZhwzW3FWCaE7Vf0qU2MYJdJ5eB0p1eimh0gnxKSQZd4"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

mashape_key = "x6adkBnZYXmshRWvj2nX0tehNLZCp1t6i54jsn3ZAARXmmZG52"
twitter_app_auth = {
    'consumer_key': 'TyIlP6mnNgQgGSmuuqGZ77SeP',
    'consumer_secret': 'KLJUO4ZssEt06GkPz1r74FA8p2FmyK0LK23pwQHSOJm5k9PpPy',
    'access_token': '2830897771-VRxmf5eYXxCcsRwjdMhmAxO89pIrBttYM5H5gx9',
    'access_token_secret': 'DfZhwzW3FWCaE7Vf0qU2MYJdJ5eB0p1eimh0gnxKSQZd4',
  }
bom = botometer.Botometer(wait_on_ratelimit=True, mashape_key=mashape_key,**twitter_app_auth)

# result = bom.check_account('@clayadavis')

# accounts = ['@clayadavis', '@onurvarol', '@jabawack']
# for screen_name, result in bom.check_accounts_in(accounts):
#     print result

user = "barackobama"
user = "@" + user

class Tweet:
    adiBot = 0
    def __init__(self, tweet, i):
        self.time = 0
        self.id = int(tweet.id_str)
        self.retweets = tweet.retweet_count
        self.favourites = tweet.favorite_count
        self.text = tweet.text
        if tweet.user.verified:
            self.userVerified = 1
        else:
            self.userVerified = 0

        self.botsFollowing = 0
        self.userFriends = tweet.user.friends_count
        self.userFollowersRatio = float(self.userFriends + 1) / (tweet.user.followers_count + 1)

botScore = bom.check_account(user)['scores']['english']
print botScore
if botScore > 0.6:
    botOrNot
# outfile = open('data.txt', 'w')
# for friend in tweepy.Cursor(api.followers,id=user).items(20):
#     json.dump(friend.screen_name, outfile)

i = 0
tweets = tweepy.Cursor(api.user_timeline,id=user).items()
# for tweet in tweets:
#     t = Tweet(tweet, i)
#     print t.time
#     print t.id
#     print t.retweets
#     print t.favourites
#     print t.text
#     print t.userVerified
#     print t.userFriends
#     print t.userFollowersRatio
#     print "\n"
#     i += 1

# Tweet.adiBot = tweets[0]
