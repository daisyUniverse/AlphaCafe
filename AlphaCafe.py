from mastodon import Mastodon
import schedule
import argparse
import random
import tweepy
import signal
import time
import json
import sys
import os

# AlphaCafe
# A simple template for a Twitter/Mastodon bot that posts random images from a folder, with optional text.
# Has the ability to simultaneously post to both Twitter and Mastodon.
# Original bot inspiration, @YKKPanels Created by @FIybyday using Cheap Bots, Done Quick!
# Reimplemented in Python by @RobinUniverse_ [R] and expanded
# 04 . 06 . 23

#Bash Color Codes:
red     = "\033[1;31m"
green   = "\033[0;32m"
yellow  = "\033[1;33m"
blue    = "\033[1;34m"
purple  = "\033[1;35m"
reset   = "\033[0;0m"

defaultConfig = {
  "TWITTER_API":{
    "ENABLED": True,
    "TWITTER_HANDLE":"@AlphaCafe",
    "CLIENT_ID":"FILL THIS OUT",
    "CLIENT_SECRET":"FILL THIS OUT",
    "CONSUMER_API_KEY":"FILL THIS OUT",
    "CONSUMER_API_SECRET":"FILL THIS OUT",
    "BEARER":"FILL THIS OUT",
    "ACCESS_TOKEN":"FILL THIS OUT",
    "ACCESS_SECRET":"FILL THIS OUT"
  },
  "MASTODON_API":{
    "ENABLED": False,
    "INSTANCE_URL":"https://botsin.space",
    "MASTODON_HANDLE":"@AlphaCafe",
    "CLIENT_KEY":"FILL THIS OUT",
    "CLIENT_SECRET":"FILL THIS OUT",
    "ACCESS_TOKEN":"FILL THIS OUT"
  },
  "DELAY_IN_MINUTES":30,
  "IMAGES_PATH":"media",
  "INIT_WITH_POST": True,
  "POST_WITH_TEXT": False,
  "TEXT_FILE": "text.txt",
  "DESCRIPTION": "An randomly chosen video or image posted by AlphaCafe",
  "RETRY_ON_ERROR": True,
  "MAX_RETRIES": 5
}

# Load config overrides from arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--delay", help="Set the delay between posts in minutes. Default is 30 minutes.", type=int)
parser.add_argument("-i", "--init", help="Set whether the bot should post immediately on startup. Default is True.", type=bool)
parser.add_argument("-t", "--text", help="Set whether the bot should post with text. Default is False.", type=bool)
parser.add_argument("-r", "--retry", help="Set whether the bot should retry on error. Default is True.", type=bool)
parser.add_argument("-m", "--max", help="Set the maximum number of retries. Default is 5.", type=int)
parser.add_argument("-c", "--config", help="Set the config file to use. Default is config.json.", type=str)
args = parser.parse_args()

# Try to load the config file. If it doesn't exist, create a default one. Also accept a config file as an argument.
try:
    if args.config:
        with open(args.config, "r") as jsonfile:
            cfg = json.load(jsonfile)
    else:
        if not os.path.exists("config.json"):
            print(red + " !!! [ERROR]: " + yellow + "config.json does not exist, creating default config." + reset)
            with open("config.json", "w") as jsonfile:
                json.dump(defaultConfig, jsonfile, indent=4)
            print(red + " !!! [ERROR]: " + yellow + "Please open config.json and fill out all API data..." + reset)
            sys.exit(1)
        with open("config.json", "r") as jsonfile:
            cfg = json.load(jsonfile)
except Exception as e:
    print(red + " !!! [ERROR]: " + yellow + "Failed to read config! Please ensure config.json exists and is valid." + reset)
    sys.exit(1)

if cfg['TWITTER_API']['CONSUMER_API_KEY'] == "FILL THIS OUT" and cfg['TWITTER_API']['ENABLED']:
    print(red + " !!! [ERROR]: " + yellow + "It looks like your Twitter API keys are not set. Please edit config.json and try again." + reset)
    sys.exit(1)

if cfg['MASTODON_API']['CLIENT_KEY'] == "FILL THIS OUT" and cfg['MASTODON_API']['ENABLED']:
    print(red + " !!! [ERROR]: " + yellow + "It looks like your Mastodon API keys are not set. Please edit config.json and try again." + reset)
    sys.exit(1)

retryCount = 0

if args.delay:
    cfg['DELAY_IN_MINUTES'] = args.delay

if args.init:
    cfg['INIT_WITH_POST'] = args.init

if args.text:
    cfg['POST_WITH_TEXT'] = args.text

if args.retry:
    cfg['RETRY_ON_ERROR'] = args.retry

if args.max:
    cfg['MAX_RETRIES'] = args.max

print( red + " >>> " + green + cfg['TWITTER_API']['TWITTER_HANDLE'] + reset + " running in AlphaCafe by @RobinUniverse_" )

# Set up Mastodon API
if cfg['MASTODON_API']['ENABLED']:
    try:
        mastodon = Mastodon(
            access_token = cfg['MASTODON_API']['ACCESS_TOKEN'],
            api_base_url = cfg['MASTODON_API']['INSTANCE_URL']
        )
    except Exception as e:
        print(red + " !!! [ERROR]: " + yellow + "Failed to connect to Mastodon API! Please ensure your config is correct." + reset)

# Set up Twitter API
if cfg['TWITTER_API']['ENABLED']:
    try:
        # Init the Twitter API V2 Client
        client = tweepy.Client(
            consumer_key        = cfg['TWITTER_API']['CONSUMER_API_KEY'],
            consumer_secret     = cfg['TWITTER_API']['CONSUMER_API_SECRET'],
            access_token        = cfg['TWITTER_API']['ACCESS_TOKEN'],
            access_token_secret = cfg['TWITTER_API']['ACCESS_SECRET']
            )
        # Set up Twitter V1 auth in order to upload the image (Not implemented in API V2)
        auth = tweepy.OAuthHandler( cfg['TWITTER_API']['CONSUMER_API_KEY'], cfg['TWITTER_API']['CONSUMER_API_SECRET'] )
        auth.set_access_token( cfg['TWITTER_API']['ACCESS_TOKEN'], cfg['TWITTER_API']['ACCESS_SECRET'] )
        api = tweepy.API(auth)
    except Exception as e:
        print(red + " !!! [ERROR]: " + yellow + "Failed to authenticate with Twitter API! Please ensure your API keys are valid." + reset)

# The Beans
def postUpdate():
    global retryCount
    text = ""

    # Upload the image and post!
    imagePath       = randomFile()
    print( "\r" +  green + " >>> " + reset + "Posting random file: '" + green + str(imagePath) + reset + "'" )

    try:
        if cfg['POST_WITH_TEXT']:
            text = randomText().replace("\n"," ")
            print( "\r" +  green + " >>> " + reset + "Posting random text: '" + green + str(text) + reset + "'" )
        
        if cfg['MASTODON_API']['ENABLED']:
            media = mastodon.media_post(imagePath)
            mastodon.status_post(text, media_ids=media, description=cfg['DESCRIPTION'])
        if cfg['TWITTER_API']['ENABLED']:
            media           = api.media_upload(imagePath)
            post_results    = client.create_tweet( media_ids=[media.media_id], text=text )
    except Exception as e:
        print(red + " !!! [ERROR]: " + yellow + str(e).replace("\n"," ") + reset)
        if cfg['RETRY_ON_ERROR'] and retryCount < cfg['MAX_RETRIES']:
            timeout = 15
            while timeout > 0:
                # Modify the same line in the terminal to show the countdown
                sys.stdout.write( red + " !!! " + reset + "Retrying in " + str(timeout) + " seconds... " + red + "(" + str(retryCount) + "/" + str(cfg['MAX_RETRIES']) + ") " + reset + "\r")
                time.sleep(1)
                timeout -= 1
            retryCount += 1
            timeout = 15
            postUpdate()
        
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

# Exit gracefully if the user presses Ctrl+C
def signal_handler(signal, frame):
    print( "\r" + red + " >>> " + reset + "Exiting AlphaCafe. Later!" )
    sys.exit(0)

# Handle signals
signal.signal(signal.SIGINT, signal_handler)

# Optionally, handle Ctrl-\ to invoke postUpdate()
def signal_handler_post(signal, frame):
    postUpdate()

signal.signal(signal.SIGQUIT, signal_handler_post)

# Return a random string of text from a specified text file to tweet, and cap the length at 280 characters.
def randomText():
    with open( cfg['TEXT_FILE'] ) as f:
        lines = f.readlines()
        randomLine = random.choice(lines)
        if len(randomLine) > 280:
            randomLine = randomLine[:280]
        return randomLine

# If the INIT_WITH_POST flag is set to true, post a tweet immediately on startup
if cfg['INIT_WITH_POST']:
    postUpdate()

# Schedule the postUpdate function to run every periodically using the schedule library ( configurable in settings.json )
schedule.every(cfg['DELAY_IN_MINUTES']).minutes.do(postUpdate)

while True:
    schedule.run_pending()
    time.sleep(10)
