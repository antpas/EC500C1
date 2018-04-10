from google.cloud import videointelligence
from google.protobuf.json_format import MessageToJson
import os
import json
import io
from google.cloud import vision
from google.cloud.vision import types
from os import listdir
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\Users\\antth\PycharmProjects\TwitterAPI\\apikey.json"


def analyze_labels():
    path = 'C:\Users\\antth\PycharmProjects\TwitterAPI\TwitterImages'

    client = vision.ImageAnnotatorClient()
    terms = []

    # for loop to go through .jpg pictures in output folder
    pictures = [pic for pic in listdir(path) if pic.endswith('jpg')]
    for picture in pictures:
        file_name = os.path.join(os.path.join(path, picture))

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        for label in labels:
            terms.append(label.description)

    return terms