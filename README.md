# AlphaCafe
### Simple configurable twitter bot for "Post random media every X minutes" style bots
AlphaBot is a simple Twitter Bot written in Python + Tweepy that is meant to be versatile enough to handle the majority of bots handled by the now defunct [Cheap Bots, Done Quick!](https://cheapbotsdonequick.com/)

You simply set up your bot account, grab your API keys, add keys and desired behaviour to the config file, and drop your text, images, and video files into a folder. The bot will handle the rest! 

Original bot inpsired by [@YKKPanels](https://twitter.com/YkkPanels) which was created by [@FIybyday](https://twitter.com/FIybyday) using [Cheap Bots, Done Quick!](https://cheapbotsdonequick.com/)


## How can I use this to create my own twitter bot?
1. create a new twitter account for your bot ( Making it's own fresh e-mail too is nice )
2. Verify your phone number with twitter
3. Go to https://developer.twitter.com/ to sign up for free access
4. Create your app, describing the purpose of the bot ( modify the existing one )
5. Go to 'User Authentication set up' to set permisions to Read+Write
6. Give it a some kind of schema ( I used `http://localhost/` )
7. Generate/Copy all access tokens into the config.json
8. Tweak config.json to your liking
9. Drop all desired media files into a subdirectory alongside the script ( these can be nested )
10. Install all required modules ( `pip install -r requirements.txt` )
11. Run the script! 

( Put it on something stable, this runs all the time. If you know how to use it, modify the service file to point to your script. )

## Twitter Bots running on AlphaCafe:
 - [@YKKBotV2](https://twitter.com/YKKBotV2) by me
 - [@ShitDominaeSays](https://twitter.com/ShitDominaeSays) by me
 
 ## CONFIG REFERENCE:
 - **TWITTER_HANDLE** : Only used in greeting for now
 - **CLIENT_ID**, **CLIENT_SECRET**, etc : Twitter API Auth
 - **IMAGES_PATH** : This is the folder in which all of your media is kept to be randomly picked from. All contents are scanned recursively, so you can have many subfolders
 - **DELAY_IN_MINUTES** : This is how many minutes you would like in between posts
 - **INIT_WITH_POST** : This will define if you would like the bot to post as soon as you start it, or wait for the timer
 - **TWEET_WITH_TEXT** : This will tell the script if you'd like to tweet a random line from a text file
 - **TEXT_FILE** : The text file in question.

This project is licensed under the [DO WHAT THE FUCK YOU WANT TO EXCEPT USE NFTS PUBLIC LICENSE](https://github.com/robinuniverse/WTFNONPL)

Note: Mastodon API compatibility + Simultanious posting planned.
