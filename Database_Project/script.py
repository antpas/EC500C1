import tweetVision
import datetime
import json
from pymongo import MongoClient
client = MongoClient()

twitterhandle = 'BU_Tweets'
num_of_tweets = 200
out = tweetVision.segment_label(twitterhandle, num_of_tweets)
keywords = []
temp = ''

try:
    for x in range(0, num_of_tweets):
        keywords.append(out['segmentLabelAnnotations'][x]['entity']['description'])
except:
    print("")

#Mongo Work
client = MongoClient('localhost', 27017)
db = client['twitter_analysis']

#Post to db
posts = db.posts
post_data = {
    'twitter_handle': twitterhandle,
    'keywords': keywords,
    'number_images': x,
    'createdon': datetime.datetime.now()
}
result = posts.insert_one(post_data)
