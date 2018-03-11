#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import botometer
import re


#Twitter API credentials

consumer_key = "TyIlP6mnNgQgGSmuuqGZ77SeP"
consumer_secret = "KLJUO4ZssEt06GkPz1r74FA8p2FmyK0LK23pwQHSOJm5k9PpPy"
access_key = "2830897771-VRxmf5eYXxCcsRwjdMhmAxO89pIrBttYM5H5gx9"
access_secret = "DfZhwzW3FWCaE7Vf0qU2MYJdJ5eB0p1eimh0gnxKSQZd4"

mashape_key = "x6adkBnZYXmshRWvj2nX0tehNLZCp1t6i54jsn3ZAARXmmZG52"
twitter_app_auth = {
    'consumer_key': 'TyIlP6mnNgQgGSmuuqGZ77SeP',
    'consumer_secret': 'KLJUO4ZssEt06GkPz1r74FA8p2FmyK0LK23pwQHSOJm5k9PpPy',
    'access_token': '2830897771-VRxmf5eYXxCcsRwjdMhmAxO89pIrBttYM5H5gx9',
    'access_token_secret': 'DfZhwzW3FWCaE7Vf0qU2MYJdJ5eB0p1eimh0gnxKSQZd4',
  }
bom = botometer.Botometer(wait_on_ratelimit=True, mashape_key=mashape_key,**twitter_app_auth)

def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    #initialize a list to hold all the tweepy Tweets
    alltweets = []
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    #save most recent tweets
    alltweets.extend(new_tweets)
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    # THIS IS THE BOTSCORE NEW!!!!!
    botScore = bom.check_account(screen_name)['scores']['english']
    verified = 0
    for t in new_tweets:
        if t.user.verified:
            verified = 1
        break

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name, count=200, max_id=oldest)
        #save most recent tweets
        alltweets.extend(new_tweets)
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        print "...%s tweets downloaded so far" % (len(alltweets))
    #transform the tweepy tweets into a 2D array that will populate the csv    
    # outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"),tweet.retweet_count,tweet.favorite_count] for tweet in alltweets]
    """outtweets = [[tweet.id_str, tweet.created_at, tweet.retweet_count,tweet.favorite_count, verified, botScore,
                  (float)(sum(1 for c in tweet.text.encode("utf-8") if c.isupper()))/len(tweet.text.encode("utf-8")),
                  sum(1 for c in tweet.text.encode("utf-8") if c=='!'),
                  tweet.text.encode("utf-8"), re.findall(r'(https?://\S+)',
                  tweet.text.encode("utf-8")), 0] for tweet in alltweets]
    """
    outtweets = [[tweet.retweet_count, tweet.favorite_count, verified, botScore,
                  (float)(sum(1 for c in tweet.text.encode("utf-8") if c.isupper())) / len(tweet.text.encode("utf-8")),
                  sum(1 for c in tweet.text.encode("utf-8") if c == '!'), 1] for tweet in alltweets]
    #write the csv    
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        #writer.writerow(["id","created_at","retweet_count","favorite_count", "verified", "botScore","Number of caps ratio","Number of Exclamations","Tweet","URLs","Fake or Not"])
        writer.writerow(
            ["retweet_count", "favorite_count", "verified", "botScore", "Number of caps ratio",
             "Number of Exclamations", "Fake or Not"])
        writer.writerows(outtweets)
    pass

if __name__ == '__main__':
    #pass in the username of the account you want to download
    user = raw_input("Enter ID: ")
    user = '@' + user
    get_all_tweets(user)
