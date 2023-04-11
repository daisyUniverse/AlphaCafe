import schedule
import random
import tweepy
import time
import json
import sys
import os

# AlphaCafe
# A simple template for a Twitter bot that posts random images from a folder, with optional text.
# Original bot inspiration, @YKKPanels Created by @FIybyday using Cheap Bots, Done Quick!
# Reimplemented in Tweepy + Python by @RobinUniverse_ [R] and expanded
# 04 . 06 . 23

# Load the JSON config file with all API goodies. If a config file is passed as an argument, use that one instead.
if sys.argv[(len(sys.argv) -1)].endswith(".json"):
    with open(sys.argv[(len(sys.argv) -1)], "r") as jsonfile:
        cfg = json.load(jsonfile)
else:
    with open("config.json", "r") as jsonfile:
        cfg = json.load(jsonfile)

#Bash Color Codes:
red     = "\033[1;31m"
green   = "\033[0;32m"
yellow  = "\033[1;33m"
blue    = "\033[1;34m"
purple  = "\033[1;35m"
reset   = "\033[0;0m"

print( red + " >>> " + green + cfg['TWITTER_HANDLE'] + reset + " running in AlphaCafe by @RobinUniverse_" )

# The Beans
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
    text = ""

    # Upload the image and tweet!
    imagePath       = randomFile()
    print( green + " >>> " + reset + "Posting random file: '" + green + str(imagePath) + reset + "'" )

    try:
        if cfg['TWEET_WITH_TEXT']:
            text = randomText().replace("\n"," ")
            print( green + " >>> " + reset + "Posting random text: '" + green + str(text) + reset + "'" )
            
        media           = api.media_upload(imagePath)
        post_results    = client.create_tweet( media_ids=[media.media_id], text=text )
    except Exception as e:
        print(red + "Error posting tweet: " + e + reset)
        time.sleep(15)
        postTweet()
        return None

# Return the path of a random panel
def randomFile():
    filepaths = []
    for dirpath, dirnames, filenames in os.walk(( cfg['IMAGES_PATH'] + "/")):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            filepaths.append(filepath)

    if not filepaths:
        return None

    randomPath = random.choice(filepaths)
    return randomPath

# Return a random string of text from a specified text file to tweet, and cap the length at 280 characters.
def randomText():
    with open( cfg['TEXT_FILE'] ) as f:
        lines = f.readlines()
        randomLine = random.choice(lines)
        if len(randomLine) > 280:
            randomLine = randomLine[:280]
        return randomLine

if cfg['INIT_WITH_POST']:
    postTweet()

# Schedule the postTweet function to run every periodically using the schedule library ( configurable in settings.json )
schedule.every(cfg['DELAY_IN_MINUTES']).minutes.do(postTweet)

while True:
    schedule.run_pending()
    time.sleep(10)


