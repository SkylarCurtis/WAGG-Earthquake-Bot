"""
Twitter class
Clean this up, it looks like trash
"""

import tweepy, os

class Twitter():
	auth = tweepy.OAuthHandler(
		os.environ['CONSUMER_PUBLIC'],
		os.environ['CONSUMER_SECRET'])
	auth.set_access_token(
		os.environ['ACCESS_KEY'],
		os.environ['ACCESS_SECRET'])
	api = tweepy.API(auth)
	def tweet(self, text): self.api.update_status(status=text)