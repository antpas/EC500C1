import tweetVision
import datetime
import psycopg2
from config import Config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE tweets (
            tweet_id SERIAL PRIMARY KEY,
            twitter_handle VARCHAR(255) NOT NULL,
            num_images INT
        )
        """,
        """
        CREATE TABLE keywords (
                tweet_id INTEGER NOT NULL,
                keyword_id SERIAL,
                keywords VARCHAR(255),
                PRIMARY KEY (tweet_id , keyword_id),
                FOREIGN KEY (tweet_id)
                    REFERENCES tweets (tweet_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    try:
        # read the connection parameters
        params = Config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(host="localhost", database="Twitter_Project", user="postgres", password="pass")
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_twitter_handle(username, imageNum):

    conn = psycopg2.connect(host="localhost", database="Twitter_Project", user="postgres", password="pass")
    cursor = conn.cursor()
    query = """INSERT INTO tweets (twitter_handle, num_images) VALUES (%s, %s);"""
    data = (username, imageNum)
    cursor.execute(query, data)
    cursor.close()
    conn.commit()


def insert_keyword(tweetId, keyword):

    conn = psycopg2.connect(host="localhost", database="Twitter_Project", user="postgres", password="pass")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO keywords (tweet_id, keywords) VALUES(%s, %s)", (tweetId, keyword))
    cursor.close()
    conn.commit()


def search_keyword_id(twitter_handle):

    conn = psycopg2.connect(host="localhost", database="Twitter_Project", user="postgres", password="pass")
    cursor = conn.cursor()
    cursor.execute("SELECT tweet_id, twitter_handle FROM tweets ORDER BY tweet_id")
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == twitter_handle:
            out = row[0]
    cursor.close()
    return out


twitterhandles = ['katyperry', 'justinbieber', 'barackobama',
                  'youtube', 'taylorswift13', 'ladygaga',
                  'elonmusk', 'richardbranson', 'realdonaldtrump',
                  'JeffBezos', 'WIRED', 'nytimes', 'FoxNews',
                  'cnnbrk', 'jimmyfallon', 'Oprah', 'KingJames',
                  'instagram', 'NASA', 'TheEconomist', 'NatGeo']

conn = psycopg2.connect(host="localhost", database="Twitter_Project", user="postgres", password="pass")
create_tables()


for i in range(0, 11):
    num_of_tweets = 100
    keywords = []

    keywords = tweetVision.analyze_labels(twitterhandles[i], num_of_tweets)
    image_count = tweetVision.cleanup()

    # Insert twitter handle and image count into tweets table
    insert_twitter_handle(twitterhandles[i], image_count)

    # Insert keywords into keywords table
    for keyword in keywords:
        tweet_id = search_keyword_id(twitterhandles[i])
        insert_keyword(tweet_id, keyword)

