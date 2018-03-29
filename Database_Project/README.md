# Twitter Image Sentiment Analysis API
This is a self contained library that helps developers more easily pull images from Twitter and run them through Google Vision. This allows for images to be searched for themes, subjects, and other identifiers.

## Getting Started
Git clone this repository to download all of the files to your local machine.

### Prerequisites
1. Python 2.7.xx
1. MongoDB
1. pymongo library


### Example
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

## Authors

* **Anthony Pasquariello** - For EC500: Building Software, Boston University 2018


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/antpas/EC500C1/blob/master/LICENSE) file for details
