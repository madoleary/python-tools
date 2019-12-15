#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Libs
#
import tweepy
import json

consumerkey = ''
consumersecret = ''
accesstoken = ''
accesstokensecret = ''

auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret)

api = tweepy.API(auth)

tweetid = ''

def perform_auth(consumerkey, consumersecret, accesstoken, accesstokensecret):
    auth = tweepy.OAuthHandler(consumerkey, consumersecret)
    auth.set_access_token(accesstoken, accesstokensecret)

    api = tweepy.API(auth)
    return api

def retweets(api, id):
    tweets = api.retweets(id)
    return tweets

def to_json(tweets):
        with open("retweets.json", "w") as write_file:
            json.dump([tweet._json for tweet in tweets], write_file)

# need to integrate click, or some other way of passing these API keys (conda?)
def main():
    api = perform_auth(consumerkey, consumersecret, accesstoken, accesstokensecret)
    tweets = retweets(api, tweetid)
    to_json(tweets)

if __name__ == "__main__":
    main()
