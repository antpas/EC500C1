# Twitter Analysis Database Project
This extends Project 1, to add database functionality. I use MongoDB in order to save data from the user. This allows for analytics to be run on the dataset. 

## Getting Started
Git clone this repository to download all of the files to your local machine.

### Prerequisites
1. Python 2.7.xx
1. MongoDB
1. pymongo library

## Overview
The project was split into two major components.
1. Develop a database schema and save image analysis of 20 different Twitter users per day (for three days)
2. Develop an analysis program to understand and gain meaningful data out of this project

### 1. Database Schema
The code that runs image analysis script on 20 Twitter users can be found in script.py file. Here's the DB schema and data gathered.
```
{
    'twitter_handle' : twitterhandle,
    'keywords' : [
        {
            'keyword' : 'redsox',
            'keyword' : baseball,
            'keyword' : 'sports'
        }
    ],
    'number_images' : x,
    'createdon' : datetime.datetime.now()
}
```

### 2. Analysis
The code that queries the database and analyses the data can be found in analysis.py file. Two queries are run here. One allows the user to search for a word and see which users have that keyword assosiated with their Tweets. The second runs a query on the database to find the most common keywords found throughout the 20 Twitter handles analyzed. Then it returns the frequency of the most popular keywords and which profiles are assosiated with that keyword. 


## Screenshots of Output
### Keyword Search: 
![alt text](https://github.com/antpas/EC500C1/blob/master/Database_Project/Data/searchword.png)

### Most Frequent Keywords
![alt text](https://github.com/antpas/EC500C1/blob/master/Database_Project/Data/mostcommon.png)

You can also find the json dump of the database after Day 1 of running the script in the /Data folder on this repo.

## Authors

* **Anthony Pasquariello** - For EC500: Building Software, Boston University 2018


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/antpas/EC500C1/blob/master/LICENSE) file for details
