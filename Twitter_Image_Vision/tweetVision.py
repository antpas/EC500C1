import convertToVideo, googleVideo, importTwitter, os


def cleanup():
    for filename in os.listdir('TwitterImages/'):
        if filename.endswith('.jpg'):
            os.remove('TwitterImages/' + filename)


def segment_label(twitter_username, tweet_count):

    importTwitter.download_images(twitter_username, tweet_count)
    convertToVideo.save()
    output = googleVideo.get_segment_labels()
    cleanup()
    return output


def shot_label(twitter_username, tweet_count):

    importTwitter.download_images(twitter_username, tweet_count)
    convertToVideo.save()
    output = googleVideo.get_shot_labels()
    cleanup()
    return output


def frame_label(twitter_username, tweet_count):

    importTwitter.download_images(twitter_username, tweet_count)
    convertToVideo.save()
    output = googleVideo.get_frame_labels()
    cleanup()
    return output
