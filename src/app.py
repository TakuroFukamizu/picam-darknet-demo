# coding: UTF-8

import sys
import os
from os.path import join, dirname
from envparse import env

from time import sleep
import picamera
from PIL import Image, ImageDraw, ImageFont
import datetime

from .configs import ROOT_DIR, DARKNET_PATH

sys.path.append(os.path.join(DARKNET_PATH, 'python'))  # darknet-nnpackのpythonバインディングを読み込む
from darknet import load_net, load_meta, detect

def detect(img_path):
    net = load_net("cfg/tiny-yolo.cfg", "tiny-yolo.weights", 0)
    meta = load_meta("cfg/coco.data")
    r = detect(net, meta, img_path)
    return r

camera = picamera.PiCamera()

def capture():
    file_name = "{0:08}.jpg".format(i)
    file_path = os.path.join(ROOT_DIR, 'captured', file_name)
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.vflip = True 
        sleep(2)
        camera.capture(file_path)
    return file_path

file_path = capture()
resutls = detect(file_path)
print(resutls)


