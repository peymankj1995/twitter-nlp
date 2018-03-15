# -*- coding: utf-8 -*-import twitter_config

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import twitter_config
from datetime import datetime
import codecs



consumer_key = twitter_config.consumer_key
consumer_secret = twitter_config.consumer_secret
access_token = twitter_config.access_token
access_secret = twitter_config.access_secret

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)



class TweetListener(StreamListener):

    def on_data(self, data):
        try:
            json_data = json.loads(data)
            # with codecs.open('tweets-'+datetime.now().strftime("%Y-%m-%d")+'.json', 'a',encoding="utf-8") as f:
            with codecs.open("tweets/"+str(json_data["id"])+'.txt', 'a',encoding="utf-8") as f:
                f.write(json_data["text"])
            print("-"*20)

            json_data = json.loads(data)
            print(json_data["text"])

            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            return False

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, TweetListener())
twitter_stream.filter(languages=['fa'], track=['با'  ])
