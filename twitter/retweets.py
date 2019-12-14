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

def json_str(tweets):
    result = json.dumps([tweet._json for tweet in tweets])
    return result

# need to integrate click, or some other way of passing these API keys (conda?)
def main():
    api = perform_auth(consumerkey, consumersecret, accesstoken, accesstokensecret)
    tweets = retweets(api, tweetid)
    json_to_dump = json_str(tweets)

    with open("tweets.json", "w") as write_file:
        json.dump(json_to_dump, write_file)

if __name__ == "__main__":
    main()