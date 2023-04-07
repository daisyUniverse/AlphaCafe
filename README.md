# YKKbotV2
### Twitter bot that posts a random panel from Yokohama Kaidashi Kikou every 30 mins. 
Original bot Created by @FIybyday using Cheap Bots, Done Quick! and then reimplemented in python by me


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

This project is licensed under the [DO WHAT THE FUCK YOU WANT TO EXCEPT USE NFTS PUBLIC LICENSE](https://github.com/robinuniverse/WTFNONPL)
