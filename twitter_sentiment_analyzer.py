# sentiment analysis by TextBlob
import tweepy
from textblob import TextBlob

consumer_key = "4JjGcRlp0hI1hDcjNGshxxulo"
consumer_secret = "EosZZi183QAmMT45qDVhPIEMfHcCNUP7622j0BpnLpzkY0CbEP"

access_token = "2436447457-PATVDY0dzEsARBECgvNTzSwpob8R30W4jN8Cyos"
access_token_secret = "NubXOzqIFkbLNyplRgHUMfs3A8EiHat2MMHfjSs8DoY7V"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)