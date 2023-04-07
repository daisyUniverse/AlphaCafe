import tweepy
import json

with open("config.json", "r") as jsonfile:
    cfg = json.load(jsonfile)

def main():
    client = tweepy.Client(
        consumer_key=cfg['CONSUMER_API_KEY'],
        consumer_secret=cfg['CONSUMER_API_SECRET'],
        access_token=cfg['ACCESS_TOKEN'],
        access_token_secret=cfg['ACCESS_SECRET']
        )

    auth = tweepy.OAuthHandler( cfg['CONSUMER_API_KEY'], cfg['CONSUMER_API_SECRET'] )
    auth.set_access_token( cfg['ACCESS_TOKEN'], cfg['ACCESS_SECRET'] )
    api = tweepy.API(auth)

    # Test Media Uploading.
    media = api.media_upload("pfp.jpg")
    tweet = "Welcome to the first test tweet of YKKBotV2! I'm writing this from scratch! if this works, hi, @RobinUniverse_!"
    post_results = client.create_tweet( text=tweet, media_ids=[media.media_id] )

if __name__ == "__main__":
    main()
