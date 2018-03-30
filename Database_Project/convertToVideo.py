import cv2
import os

def save():
    os.system('ffmpeg -y -loglevel panic -framerate 1/3 -i TwitterImages\image%d.jpg video.avi')