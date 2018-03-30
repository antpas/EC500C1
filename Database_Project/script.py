import tweetVision
import datetime
from pymongo import MongoClient
client = MongoClient()


twitterhandles = ['katyperry', 'justinbieber', 'barackobama',
                  'youtube', 'taylorswift13', 'ladygaga',
                  'elonmusk', 'richardbranson', 'realdonaldtrump',
                  'JeffBezos', 'WIRED', 'nytimes','FoxNews',
                  'cnnbrk', 'jimmyfallon', 'Oprah', 'KingJames',
                  'instagram', 'NASA', 'TheEconomist', 'NatGeo']

for i in range(0, 21):
    num_of_tweets = 100
    keywords = []

    keywords = tweetVision.analyze_labels(twitterhandles[i], num_of_tweets)
    image_count = tweetVision.cleanup()

    #Mongo Work
    client = MongoClient('localhost', 27017)
    db = client['twitter_analysis']

    #Post to db
    posts = db.posts
    post_data = {
        'twitter_handle': twitterhandles[i],
        'keywords': keywords,
        'number_images': image_count,
        'createdon': datetime.datetime.now()
    }
    result = posts.insert_one(post_data)
