import cv2
import os

def save():
    os.system('ffmpeg -framerate 1/3 -i TwitterImages\image%d.jpg video.avi')
save()
