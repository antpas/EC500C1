# Twitter Image Sentiment Analysis API
This is a self contained library that helps developers more easily pull images from Twitter and run them through Google Vision. This allows for images to be searched for themes, subjects, and other identifiers.

## Getting Started
Git clone this repository to download all of the files to your local machine.

### Prerequisites
1. Python 2.7.xx
1. tweepy (API)
1. ffmpy (Installed On Machine)
1. Google Video Intelligence (API)

### Installing Prereqs

Install Python
* Follow instructions on: [a link](https://www.python.org/downloads)

Install Tweepy
```
pip install tweepy
```

Install FFmpeg
* Windows:
** Donwload FFmpeg here: [a link](https://www.ffmpeg.org/download.html#build-windows)
** Put the contents of the download in a folder called ffmpeg at root location C:\
* OSX
** Donwload FFmpeg here: [a link](https://www.ffmpeg.org/download.html#build-mac)
** Put the contents of the download in a folder called ffmpeg at root location C:\
* Other tutorials to download ffmpeg
** [a link] (http://www.renevolution.com/ffmpeg/2013/03/16/how-to-install-ffmpeg-on-mac-os-x.html)

### API Setup
* Create a Google Cloud Intelligence API key (as a service account). 
** Download the json key file, name it apikey.json
** Put it in the root project folder
* Create twitter API credentials
** Copy the keys (four of them) into the passwords.py file

## Setup Files in this repo 
* Copy all files from this repo to the project folder you want to use it in
googleVideo.py
```
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="<Path to project>\\apikey.json"
```
passwords.py
```
consumer_key = 'Put key here'
consumer_secret = 'key here'
access_token = 'key here'
access_secret = 'key here'
```


## Authors

* **Anthony Pasquariello** - For EC500: Building Software, Boston University 2018


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
