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
    serial = MessageToJson(result)
    output = json.loads(serial)

    return output['annotationResults'][0]


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

    return result


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

    return result

