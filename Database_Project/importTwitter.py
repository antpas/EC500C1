import tweepy
from tweepy import OAuthHandler
import json
import wget
import os

# import secret key from local file called passwords.py (not pushed to github)
from passwords import consumer_key, consumer_secret, access_token, access_secret


# Setup
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status


tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse

tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def download_images(twitter_name, tweet_count):
    # Tweet gathering
    tweets = api.user_timeline(screen_name=twitter_name,
                               count=tweet_count, include_rts=False,
                               exclude_replies=True)

    # Get imgaes
    media_files = set()
    for status in tweets:
        media = status.entities.get('media', [])
        if (len(media) > 0):
            media_files.add(media[0]['media_url'])

    if not os.path.exists('TwitterImages'):
        os.makedirs('TwitterImages')

    # Download images
    count = 0
    for media_file in media_files:
        wget.download(media_file, out='TwitterImages/image' + str(count) + '.jpg')
        count = count + 1

