# AlphaCafe
### Simple configurable twitter bot for "Post random media every X minutes" style bots
AlphaCafe is a Twitter and Mastodon Bot written in Python that is meant to be both simple enough to easily be modified and versatile enough to handle the majority of bots handled by the now defunct [Cheap Bots, Done Quick!](https://cheapbotsdonequick.com/) out of the box

You simply set up your bot account, grab your API keys, add keys and desired behaviour to the config file, and drop your text, images, and video files into a folder. The bot will handle the rest! 

Original bot inpsired by [@YKKPanels](https://twitter.com/YkkPanels) which was created by [@FIybyday](https://twitter.com/FIybyday) using [Cheap Bots, Done Quick!](https://cheapbotsdonequick.com/)

![image](https://user-images.githubusercontent.com/12601774/231315740-7f889fd2-5a31-4f86-859e-815f09d36d63.png)

## How can I use this to create my own Twitter bot?
1. [Create a new twitter account](https://twitter.com/i/flow/signup) for your bot ( you need to be signed out to do this )
2. Verify your phone number with twitter
3. Mark your bot account as automated and link it to your main account ( Settings > Account Information > Automation )
4. Go to the [Twitter developer portal](https://developer.twitter.com/) and sign up for free access
5. Create your app, describing the purpose of the bot ( modify the existing one )
6. Go to 'User Authentication set up' to set permisions to Read + Write
7. Give it a some kind of schema ( I use `http://localhost/` )
8. Generate/Copy all auth tokens/keys/secrets/etc into the config.json
9. Tweak config.json to your liking
10. Drop all desired media files into a subdirectory alongside the script ( these can be nested )
11. Install all required modules ( `pip install -r requirements.txt` )
12. Run the script! 

## How can I use this to create my own Mastodon bot?
1. Create a new Mastodon account for your bot ( I like using [botsin.space](https://botsin.space) )
2. Once approved, go to profile settings and mark as a bot account
3. In settings, go to the Development tab, and click create new application. Leave settings as default.
4. Copy your API stuff into the config, end change enabled to true
5. Install all required modules ( `pip install -r requirements.txt` )
6. Run the script!

If you have both Twitter and Mastodon enabled, the posts will be mirrored across both platforms.

( Put it on something stable, this runs all the time. If you know how to use it, modify the service file to point to your script. This will ensure that the script gets started on bootup, and automatically restarts in case of a crash )

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

## ARGS
AlphaCafe accepts a number of Args. These will override what exists in the currently used configfile, even if a new one is defined in args.

```
  -d DELAY,  --delay  DELAY     Set the delay between posts in minutes. Default is 30 minutes.
  -i INIT,   --init   INIT      Set whether the bot should post immediately on startup. Default is True.
  -t TEXT,   --text   TEXT      Set whether the bot should post with text. Default is False.
  -r RETRY,  --retry  RETRY     Set whether the bot should retry on error. Default is True.
  -m MAX,    --max    MAX       Set the maximum number of retries. Default is 5.
  -c CONFIG, --config CONFIG    Set the config file to use. Default is config.json.
```

Ctrl-C (SIGINT) to exit. Ctrl-\ (SIGQUIT) to instantly post a new update.

This project is licensed under the [DO WHAT THE FUCK YOU WANT TO EXCEPT USE NFTS PUBLIC LICENSE](https://github.com/robinuniverse/WTFNONPL)
