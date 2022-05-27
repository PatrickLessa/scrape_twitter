# -*- coding: utf-8 -*-
import tweepy
from dotenv import load_dotenv
import os
from collections import namedtuple
from factory.cleanTweets import clean

class Twitter:

    def __init__(self):
        load_dotenv()
        self.client = tweepy.Client(os.getenv("BEARER_TOKEN"))

    def searchTweets(self, words):
        query = f"#{words} lang:pt -is:retweet"
        tweets_list = []
        Tweet = namedtuple("Tweet", ["id", "name", "text", "likes", "retweets", "created_at", "source"])
        for response in tweepy.Paginator(
            self.client.search_recent_tweets,
            query=query,
            tweet_fields=['entities','context_annotations', 'created_at', 'public_metrics', 'source', 'geo', 'referenced_tweets'],
            max_results=100,  
            place_fields = ['place_type', 'geo'],
            expansions=['author_id', 'geo.place_id', 'referenced_tweets.id.author_id', 'referenced_tweets.id']
        ):
            users = { user.id: user for user in response.includes["users"] }
            for tweet in response.data:
                if users[tweet.author_id]:
                    user = users[tweet.author_id]
                    tweets_list.append(Tweet(tweet.id,
                                            user.name, 
                                            clean(tweet.text), 
                                            tweet.public_metrics['like_count'], 
                                            tweet.public_metrics['retweet_count'], 
                                            tweet.created_at.strftime('%d-%m-%Y %H:%M:%S'), 
                                            tweet.source
                                            )
                                        )
        return tweets_list
            