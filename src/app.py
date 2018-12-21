# coding: UTF-8

import sys
import os
from time import sleep
import picamera
from datetime import datetime

from configs import ROOT_DIR, DARKNET_PATH
from darknet import load_net, load_meta, detect

def detect(img_path):
    net = load_net(os.path.join(DARKNET_PATH, "cfg/tiny-yolo.cfg"), os.path.join(DARKNET_PATH, "tiny-yolo.weights"), 0)
    meta = load_meta(os.path.join(DARKNET_PATH, "cfg/coco.data"))
    r = detect(net, meta, img_path)
    return r

camera = picamera.PiCamera()

def capture():
    file_name = "{}.jpg".format(datetime.now().strftime("%Y%m%d-%H%M%S"))
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


