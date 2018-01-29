import cv2
import os

def save():
    os.system('ffmpeg -r .5 -i TwitterImages\image%d.jpg -vcodec mpeg4 -y video.mp4')

save()
