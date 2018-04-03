import collections
from pprint import pprint
from pymongo import MongoClient

client = MongoClient()

client = MongoClient('localhost', 27017)
db = client['twitter_analysis']


# Find which users have specific keyword
search_word = "fun"
cursor = db.posts.find({"keywords": search_word})
print("{} {}".format("Search Word:", search_word))
for document in cursor:
    pprint(document["twitter_handle"])


# Find most popular keywords across all twitter handles
counter = collections.Counter(document["keywords"])
common_keyword = []
common_keyword = counter.most_common()
print("")
print("")
print("Most common keywords:")
print("")
for k, v in common_keyword:
    if v > 1:
        print("Keyword/Frequency")
        print(k, v)
        search_word = k
        cursor = db.posts.find({"keywords": search_word})
        print("Assosiated Twitter Handle(s): ")
        for document in cursor:
            pprint(document["twitter_handle"])
        print(" ")