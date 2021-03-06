#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import bottle
from backend.routes import app
from backend.configs import ROOT_DIR, DARKNET_PATH, DARKNET_CONFIG_FILE, DARKNET_WEIGHT_FILE, DARKNET_DATASET_FILE
# from darknet import load_net, load_meta, detect
from backend.darknet import exec_darknet, YoloConfig
from backend.camera import capture
from loggingcap import capture_and_logging


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
    parser.add_argument("--logging_mode", action='store_true', required=False)
    parser.add_argument("--logging_output_dir", required=False)
    args, unknown_args = parser.parse_known_args()
    demo_mode = args.demo_mode
    server_mode = args.server_mode
    logging_mode = args.server_mode
    logging_output_dir = args.logging_output_dir

    config = YoloConfig()
    config.config_file = DARKNET_CONFIG_FILE
    config.weights_file = DARKNET_WEIGHT_FILE
    config.dataset_file = DARKNET_DATASET_FILE
    
    if server_mode:
        # bottle.run(app=app, port=8080, host='0.0.0.0', reloader=True, debug=True, server='cherrypy')
        bottle.run(app=app, port=8080, host='0.0.0.0', reloader=True, debug=True)
    
    elif logging_mode:
        capture_time = 3
        capture_and_logging(config, logging_output_dir, capture_time)

    else:
        file_path = None
        if not demo_mode:
            file_path = capture()
        else:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'my_picture.jpg'))
        resutls = detect(config, file_path)
        print(resutls)



 


