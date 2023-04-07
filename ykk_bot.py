import random
import tweepy
import json
import os
import schedule
import time

# A simple Twitter bot that posts a random image every 30 minutes
# Original bot Created by @FIybyday using Cheap Bots, Done Quick!
# Reimplemented in Tweepy + Python by @RobinUniverse_ [R]
# 04 . 06 . 23

# Load the JSON config file with all API goodies.
with open("config.json", "r") as jsonfile:
    cfg = json.load(jsonfile)

def postTweet():

    # Init the Twitter API V2 Client
    client = tweepy.Client(
        consumer_key        = cfg['CONSUMER_API_KEY'],
        consumer_secret     = cfg['CONSUMER_API_SECRET'],
        access_token        = cfg['ACCESS_TOKEN'],
        access_token_secret = cfg['ACCESS_SECRET']
        )

    # Set up Twitter V1 auth in order to upload the image (Not implemented in API V2)
    auth = tweepy.OAuthHandler( cfg['CONSUMER_API_KEY'], cfg['CONSUMER_API_SECRET'] )
    auth.set_access_token( cfg['ACCESS_TOKEN'], cfg['ACCESS_SECRET'] )
    api = tweepy.API(auth)

    # Upload the image and tweet!
    media           = api.media_upload(randomPanel())
    post_results    = client.create_tweet( media_ids=[media.media_id] )

# Return the path of a random panel
def randomPanel():
    directory_path = 'Panels'
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    for dirpath, dirnames, filenames in os.walk(directory_path):
        image_files = [f for f in filenames if f.lower().endswith(image_extensions)]
        if image_files:
            random_image = random.choice(image_files)
            return os.path.join(dirpath, random_image)
    return None

schedule.every(30).minutes.do(postTweet)

while True:
    schedule.run_pending()
    time.sleep(10)
