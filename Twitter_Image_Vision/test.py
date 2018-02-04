import tweetVision

out = tweetVision.segment_label('BU_Tweets', 100)
print(out['segmentLabelAnnotations'][0]['entity']['description'])
print(out['segmentLabelAnnotations'][1]['entity']['description'])


# Use tweetVision.segment_label normally
# I use frame_label here as an example (b/c json is nicer in frame_label)
# Same information from both
print('JSON Format: ')
print(tweetVision.frame_label('BU_Tweets', 100))
