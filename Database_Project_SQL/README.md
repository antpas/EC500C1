# Twitter Analysis SQL Database Project
This extends Project 1, to add database functionality. For Phase 2, I now use PostgresSQL in order to save data from the user. This allows for analytics to be run on the dataset. 

## Getting Started
Git clone this repository to download all of the files to your local machine.

### Prerequisites
1. Python 2.7.xx
1. PostgresSQL
1. import psycopg2

## Overview
The project was split into two major components.
1. Develop a database schema and save image analysis of 20 different Twitter users per day
2. Develop an analysis program to understand and gain meaningful data out of this project
3. Understand the differences between relational DB (this project) and non-relational DB (MongoDB)

## Database Schema
Two Tables:
1. tweets
2. keywords

As you can see from images below, the tweets table has three columns: tweet_id, twitter_handle, num_images.
The keywords table inherits the tweet_id from the corresponding twitter account associated with those keywords. It also has the keyword_id, and keyword.

### Tweets Table
![alt text](https://github.com/antpas/EC500C1/blob/master/Database_Project_SQL/Data/tweetsTable.png)

### Keywords Table
![alt text](https://github.com/antpas/EC500C1/blob/master/Database_Project_SQL/Data/keywordsTable.png)
![alt text](https://github.com/antpas/EC500C1/blob/master/Database_Project_SQL/Data/keywordsTable2.png)

### 2. Analysis
The code that queries the database and analyses the data can be found in analysis.py file. A query is run on the database to find the most common keywords found throughout the 20 Twitter handles analyzed. Then it returns the frequency of the most popular keywords.


## Screenshots of Output
### Keyword Search: 
![alt text](https://github.com/antpas/EC500C1/blob/master/Database_Project_SQL/Data/mostfreq.png)


## Authors

* **Anthony Pasquariello** - For EC500: Building Software, Boston University 2018


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/antpas/EC500C1/blob/master/LICENSE) file for details
