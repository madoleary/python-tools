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

def construct_custom_json_object(tweet_json):
    custom_format_tweet = {
        "retweet_id": tweet_json["id"],
        "retweet_text": tweet_json["text"],
        "retweet_favorite_count": tweet_json["favorite_count"],
        "is_retweet_retweeted": tweet_json["retweeted"],
        "user_retweeted": {
          "user_id": tweet_json["retweeted_status"]["user"]["id"],
          "user_id_str": tweet_json["retweeted_status"]["user"]["id_str"],
          "verified": tweet_json["retweeted_status"]["user"]["verified"],
          "followers_count": tweet_json["retweeted_status"]["user"]["followers_count"],
          "statuses_count": tweet_json["retweeted_status"]["user"]["statuses_count"],
          "description": tweet_json["retweeted_status"]["user"]["description"],
          "name": tweet_json["retweeted_status"]["user"]["name"],
          "friends_count": tweet_json["retweeted_status"]["user"]["friends_count"],
          "screen_name": tweet_json["retweeted_status"]["user"]["screen_name"],
          "created_at": tweet_json["retweeted_status"]["user"]["created_at"],
          "location": tweet_json["retweeted_status"]["user"]["location"],
          "followed_by_retweeter": tweet_json["retweeted_status"]["user"]["following"]
        },
        "retweet_user": {
          "user_id": tweet_json["user"]["id"],
          "user_id_str": tweet_json["user"]["id_str"],
          "verified": tweet_json["user"]["verified"],
          "profile_image_url_https": tweet_json["user"]["profile_image_url_https"],
          "followers_count": tweet_json["user"]["followers_count"],
          "statuses_count": tweet_json["user"]["statuses_count"],
          "description": tweet_json["user"]["description"],
          "friends_count": tweet_json["user"]["friends_count"],
          "location": tweet_json["user"]["location"],
          "followed_by_retweeted_user": tweet_json["user"]["followed_by"],
          "profile_background_image_url": tweet_json["user"]["profile_background_image_url"],
          "screen_name": tweet_json["user"]["screen_name"],
          "name": tweet_json["user"]["name"],
          "created_at": tweet_json["user"]["created_at"]
        }
    }

    return custom_format_tweet


def to_json(tweets):
    for tweet in tweets:
        tweet_json = tweet._json
        formatted_tweet_json = construct_custom_json_object(tweet_json)

        with open("retweets-formatted.json", "w") as write_file:
            json.dump(formatted_tweet_json, write_file)

# need to integrate click, or some other way of passing these API keys (conda?)
def main():
    api = perform_auth(consumerkey, consumersecret, accesstoken, accesstokensecret)
    tweets = retweets(api, tweetid)
    to_json(tweets)

if __name__ == "__main__":
    main()
