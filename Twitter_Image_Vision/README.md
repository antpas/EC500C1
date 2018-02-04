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
- Follow instructions on: [Python Download](https://www.python.org/downloads)

Install Tweepy
```
pip install tweepy
```

Install FFmpeg
- Windows:
  - Donwload FFmpeg here: [FFmpeg Download](https://www.ffmpeg.org/download.html#build-windows)
  - Put the contents of the download in a folder called ffmpeg at root location C:\
- OSX
  - Donwload FFmpeg here: [FFmpeg Download](https://www.ffmpeg.org/download.html#build-mac)
  - Put the contents of the download in a folder called ffmpeg at root location C:\
- Other tutorials to download ffmpeg
  - [FFmpeg Tutorial] (http://www.renevolution.com/ffmpeg/2013/03/16/how-to-install-ffmpeg-on-mac-os-x.html)

### API Setup
- Create a Google Cloud Intelligence API key (as a service account). 
  - Download the json key file, name it apikey.json
  - Put it in the root project folder
- Create twitter API credentials
  - Copy the keys (four of them) into the passwords.py file

## Setup Files in this repo 
- Copy all files from this repo to the project folder you want to use it in

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

## Usage Documentation

### Main wrapper file
The main file that the developer interacts with is tweetVision.py

### Example how to use main wrapper
- See test.py in this repo

### General Use Example
Import tweetVision to file you want to use it in
```
import tweetVision
```

In that file you can use it like such:
```
out = tweetVision.segment_label('BU_Tweets', 100)
```

### Data Output Format
The output format is JSON:
```
annotation_results {
  segment_label_annotations {
    entity {
      entity_id: "/m/06_dn"
      description: "snow"
      language_code: "en-US"
    }
    category_entities {
      entity_id: "/m/0866r"
      description: "weather"
      language_code: "en-US"
    }
    segments {
      segment {
        start_time_offset {
        }
        end_time_offset {
          seconds: 9
        }
      }
      confidence: 0.428644835949
    }
  }
  segment_label_annotations {
    entity {
      entity_id: "/m/086mh"
      description: "winter"
      language_code: "en-US"
    }
    category_entities {
      entity_id: "/m/0754v"
      description: "season"
      language_code: "en-US"
    }
    segments {
      segment {
        start_time_offset {
        }
        end_time_offset {
          seconds: 9
        }
      }
      confidence: 0.572898983955
    }
  }
  shot_label_annotations {
    entity {
      entity_id: "/m/07j7r"
      description: "tree"
      language_code: "en-US"
    }
    category_entities {
      entity_id: "/m/05s2s"
      description: "plant"
      language_code: "en-US"
    }
    segments {
      segment {
        start_time_offset {
          seconds: 3
        }
        end_time_offset {
          seconds: 9
        }
      }
      confidence: 0.419648438692
    }
  }
  shot_label_annotations {
    entity {
      entity_id: "/m/06_dn"
      description: "snow"
      language_code: "en-US"
    }
    category_entities {
      entity_id: "/m/0866r"
      description: "weather"
      language_code: "en-US"
    }
    segments {
      segment {
        start_time_offset {
          seconds: 3
        }
        end_time_offset {
          seconds: 9
        }
      }
      confidence: 0.73469388485
    }
  }
  shot_label_annotations {
    entity {
      entity_id: "/m/086mh"
      description: "winter"
      language_code: "en-US"
    }
    category_entities {
      entity_id: "/m/0754v"
      description: "season"
      language_code: "en-US"
    }
    segments {
      segment {
        start_time_offset {
          seconds: 3
        }
        end_time_offset {
          seconds: 9
        }
      }
      confidence: 0.787180364132
    }
  }
}
```

This data can easily be used by accessing the JSON object.

### Example
```
import tweetVision

out = tweetVision.segment_label('BU_Tweets', 100)
print(out['segmentLabelAnnotations'][0]['entity']['description'])
print(out['segmentLabelAnnotations'][1]['entity']['description'])
```

## Authors

* **Anthony Pasquariello** - For EC500: Building Software, Boston University 2018


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/antpas/EC500C1/blob/master/LICENSE) file for details
