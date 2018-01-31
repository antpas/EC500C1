from google.cloud import videointelligence
import os
import io
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="Path\to\json\key\apikey.json"


def get_segment_labels():

    path = os.path.join(os.path.dirname(__file__), 'video.avi')
    if not os.path.exists(path):
        raise ValueError('No images available')

    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]

    with io.open(path, 'rb') as movie:
        input_content = movie.read()

    operation = video_client.annotate_video(features=features, input_content=input_content)

    result = operation.result(timeout=90)

    # Process video/segment level label annotations
    segment_labels = result.annotation_results[0].segment_label_annotations

    return segment_labels


def get_shot_labels():
    path = os.path.join(os.path.dirname(__file__), 'video.avi')
    if not os.path.exists(path):
        raise ValueError('No images available')

    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]

    with io.open(path, 'rb') as movie:
        input_content = movie.read()

    operation = video_client.annotate_video(features=features, input_content=input_content)

    result = operation.result(timeout=90)

    # Process shot level label annotations
    shot_labels = result.annotation_results[0].shot_label_annotations

    return shot_labels


def get_frame_labels():

    path = os.path.join(os.path.dirname(__file__), 'video.avi')
    if not os.path.exists(path):
        raise ValueError('No images available')

    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]

    with io.open(path, 'rb') as movie:
        input_content = movie.read()

    operation = video_client.annotate_video(features=features, input_content=input_content)

    result = operation.result(timeout=90)

    # Process frame level label annotations
    frame_labels = result.annotation_results[0].frame_label_annotations

    return frame_labels


