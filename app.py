#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import bottle
from src.routes import app
from src.configs import ROOT_DIR, DARKNET_PATH
# from darknet import load_net, load_meta, detect
from src.darknet import exec_darknet, YoloConfig
from src.camera import capture


def detect(config: YoloConfig, img_path: str):
    # net = load_net(config.config_file, config.weights_file, 0)
    # meta = load_meta(config.dataset_file)
    # r = detect(net, meta, img_path)
    # .so is not working now.
    r = exec_darknet(config, img_path)
    return r

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo_mode", action='store_true', required=False)
    parser.add_argument("--server_mode", action='store_true', required=False)
    args, unknown_args = parser.parse_known_args()
    demo_mode = args.demo_mode
    server_mode = args.server_mode

    config = YoloConfig()
    config.config_file = os.path.join(DARKNET_PATH, "cfg/yolov3-tiny.cfg")
    config.weights_file = os.path.join(DARKNET_PATH, "yolov3-tiny.weights")
    config.dataset_file = os.path.join(DARKNET_PATH, "cfg/coco.data")
    
    if not server_mode:
        file_path = None
        if not demo_mode:
            file_path = capture()
        else:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'my_picture.jpg'))
        resutls = detect(config, file_path)
        print(resutls)
    else:
        bottle.run(app=app, port=8080, host='0.0.0.0', reloader=True, debug=True)



 


