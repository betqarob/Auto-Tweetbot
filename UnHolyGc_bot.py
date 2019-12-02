#You need to install tweepy into your computer for it to work as you code
#only works with Python 2 to 3.7
#Website to get Tweepy installed:  https://github.com/tweepy/tweepy/issues/1063
#use this command on your command line in order to install Tweepy:   pip install -U git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b
#Try "pip3" first to see if that works, if not use "pip"

import tweepy
import time
import random

# Note: Whenever you want your bot to run on twitter, you need to have the file open in order for it to work throughout the time you had your computer turned on.
a = ""
b = ""
c = ""
d = ""
e = ""
f = ""
#array is used to tweet things randomly. 
tweet_array = [a, b, c, d, e, f]


#creditionals to login into Twitter API
consumer_key = "" # you need consumer key 
consumer_secret = "" # you need consumer secret key 
access_token = "" # you need the access token
access_token_secret = "" # you need the access token secret 

#all of this is needed from the website: https://developer.twitter.com/en.html and you need to sign up for the developer account

#login into Twitter account API
def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Expection as e:
        return None
oauth = OAuth()
api = tweepy.API(oauth)

#tweets that are sent to the Twitter Tweeting API
for xyz in tweet_array:
    api.update_status(random.choice(tweet_array))
    print('a tweet has been made :D')
    time.sleep (1800) # the timer is optional but recommended in order to avoid getting your account terminated. You can't really be spamming on twitter.
