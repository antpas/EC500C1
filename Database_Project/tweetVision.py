import convertToVideo, googleVideo, importTwitter, os


def cleanup():

    count = 0
    for filename in os.listdir('TwitterImages/'):
        count = count + 1
        if filename.endswith('.jpg'):
            os.remove('TwitterImages/' + filename)
    return count

def analyze_labels(twitter_username, tweet_count):

    importTwitter.download_images(twitter_username, tweet_count)
    convertToVideo.save()
    output = googleVideo.analyze_labels()
    return output
