import tweepy

user = raw_input("Enter account name: ")
user = "@" + user

consumer_key = "TyIlP6mnNgQgGSmuuqGZ77SeP"
consumer_secret = "KLJUO4ZssEt06GkPz1r74FA8p2FmyK0LK23pwQHSOJm5k9PpPy"
access_token_key = "2830897771-VRxmf5eYXxCcsRwjdMhmAxO89pIrBttYM5H5gx9"
access_token_secret = "DfZhwzW3FWCaE7Vf0qU2MYJdJ5eB0p1eimh0gnxKSQZd4"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

class Tweet:
    userFriends = 0
    userFollowersRatio = 0
    i = 0
    def __init__(self, tweet):
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

        if i == 0:
            userFriends = tweet.user.friends_count
            userFollowersRatio = float(userFriends) / tweet.user.followers_count
        i += 1

    def getI(self):
        print i


for tweet in tweepy.Cursor(api.user_timeline,id=user).items():
    t = Tweet(tweet)
    print t.time
    print t.id
    print t.retweets
    print t.favourites
    print t.text
    print t.userVerified
    print t.userFriends
    print t.userFollowersRatio
    print "\n"

