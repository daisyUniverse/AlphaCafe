# AlphaCafe
### Basic Template for simple twitter bots
Original bot inspiration: @YKKPanels created by @FIybyday using Cheap Bots, Done Quick! and then reimplemented and expanded in python by me


I wanted to go ahead and put this on github to give people a solid starting out point to make similar bots in the future. This is roughly the method that I used.

1. create a new twitter account for your bot ( Making it's own fresh e-mail too is nice )
2. Verify your phone number with twitter
3. Go to https://developer.twitter.com/ to sign up for free access
4. Create your app, describing the purpose of the bot ( modify the existing one )
5. Copy/Regenerate all keys and tokens into a config file
6. Go to 'User Authentication set up' to set permisions to Read+Write
7. Give it a some kind of schema ( I used `http://localhost/` )
8. Generate a new Access Token + Secret and save them in your config file
9. Using tweepy, set up both auth for V1 and V2 apis using the method seen in my script
10. Use API V1 to upload the image and use API V2 to post the tweet

I have expanded this bot in order to make it work for many more situations depending on configuration, you only need to fill out the config file

## Twitter Bots running on AlphaCafe:
 - [@YKKBotV2](https://twitter.com/YKKBotV2) by me
 - [@ShitDominaeSays](https://twitter.com/ShitDominaeSays) by me
 
 ## CONFIG REFERENCE:
 - **BOTNAME** : Only used in greeting for now, but could be expanded
 - **CLIENT_ID**, **CLIENT_SECRET**, etc : Twitter API Auth
 - **IMAGES_PATH** : This is the folder in which all of your media is kept to be randomly picked from. All contents are scanned recursively, so you can have many subfolders
 - **DELAY_IN_MINUTES** : This is how many minutes you would like in between posts
 - **INIT_WITH_POST** : This will define if you would like the bot to post as soon as you start it, or wait for the timer
 - **TWEET_WITH_TEXT** : This will tell the script if you'd like to tweet a random line from a text file
 - **TEXT_FILE** : The text file in question.

This project is licensed under the [DO WHAT THE FUCK YOU WANT TO EXCEPT USE NFTS PUBLIC LICENSE](https://github.com/robinuniverse/WTFNONPL)
