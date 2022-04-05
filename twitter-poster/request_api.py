import json
import requests

class my_Twitter:
    def __init__(self, endpoint, headers, payload):
        self.endpoint = endpoint
        self.headers = headers
        self.payload = payload
       
    
    def get_tweet(self, tweet_id):
        self.tweet_id = tweet_id
        return requests.get(f"{self.endpoint}/{tweet_id}", headers=self.headers, data=self.payload)

    def get_10_tweets(self, user_id):
        self.user_id = user_id
        return requests.get(f"{self.endpoint}/{user_id}/tweets", headers=self.headers, data=self.payload)

    def _get_user_id(self, username):
        self.username = username
        return requests.get(f"{self.endpoint}/{username}", headers=self.headers, data=self.payload)


    def post_tweet(self, tweet):
        self.tweet = tweet
        self.payload = json.dumps({
            "text": self.tweet
        })
        return requests.post(f"{self.endpoint}", headers=self.headers, data=self.payload)