# coding: UTF-8

import sys
import os
import argparse
from time import sleep
from datetime import datetime

from src.configs import ROOT_DIR, DARKNET_PATH
# from darknet import load_net, load_meta, detect
from src.darknet import exec_darknet, YoloConfig


def detect(config: YoloConfig, img_path: str):
    # net = load_net(config.config_file, config.weights_file, 0)
    # meta = load_meta(config.dataset_file)
    # r = detect(net, meta, img_path)
    # .so is not working now.
    r = exec_darknet(config, img_path)
    return r

def capture():
    import picamera
    file_name = "{}.jpg".format(datetime.now().strftime("%Y%m%d-%H%M%S"))
    file_path = os.path.join(ROOT_DIR, 'captured', file_name)
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.vflip = True 
        sleep(2)
        camera.capture(file_path)
    return file_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo_mode", action='store_true', required=False)
    args, unknown_args = parser.parse_known_args()
    demo_mode = args.demo_mode

    config = YoloConfig()
    config.config_file = os.path.join(DARKNET_PATH, "cfg/yolov3-tiny.cfg")
    config.weights_file = os.path.join(DARKNET_PATH, "yolov3-tiny.weights")
    config.dataset_file = os.path.join(DARKNET_PATH, "cfg/coco.data")
    
    file_path = None
    if not demo_mode:
        file_path = capture()
    else:
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'my_picture.jpg'))
    resutls = detect(config, file_path)
    print(resutls)


