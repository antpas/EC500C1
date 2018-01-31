import convertToVideo, googleVideo, importTwitter


def segment_label(twitter_username, tweet_count):

    importTwitter.download_images(twitter_username, tweet_count)
    convertToVideo.save()
    output = googleVideo.get_segment_labels()

    return output


def shot_label(twitter_username, tweet_count):

    importTwitter.download_images(twitter_username, tweet_count)
    convertToVideo.save()
    output = googleVideo.get_shot_labels()

    return output


def frame_label(twitter_username, tweet_count):

    importTwitter.download_images(twitter_username, tweet_count)
    convertToVideo.save()
    output = googleVideo.get_frame_labels()

    return output

