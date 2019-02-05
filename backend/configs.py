# -*- coding: utf-8 -*-

import sys
import os
from envparse import env

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

TEMP_CAPTURED_DIR = os.path.join(ROOT_DIR, 'captured')

## from dotenv
env.read_envfile(os.path.join(ROOT_DIR, '.env'))
DARKNET_PATH = env.str("DARKNET_PATH", default='')

USER_DARKNET_LABEL_FILE = env.str("USER_DARKNET_LABEL_FILE", default='')
USER_DARKNET_CONFIG_FILE = env.str("USER_DARKNET_CONFIG_FILE", default='')
USER_DARKNET_WEIGHT_FILE = env.str("USER_DARKNET_WEIGHT_FILE", default='')

if len(USER_DARKNET_LABEL_FILE) > 0 and len(USER_DARKNET_CONFIG_FILE) > 0 and len(USER_DARKNET_WEIGHT_FILE):
    USER_DARKNET_LABEL_FILE = os.path.join(ROOT_DIR, USER_DARKNET_LABEL_FILE)
    USER_DARKNET_CONFIG_FILE = os.path.join(ROOT_DIR, USER_DARKNET_CONFIG_FILE)
    USER_DARKNET_WEIGHT_FILE = os.path.join(ROOT_DIR, USER_DARKNET_WEIGHT_FILE)


# DARKNET_LABEL_FILE = os.path.join(DARKNET_PATH, "manacamera/labels.txt")
# DARKNET_CONFIG_FILE = os.path.join(DARKNET_PATH, "manacamera/yolo3-tiny.cfg")
# DARKNET_WEIGHT_FILE = os.path.join(DARKNET_PATH, "manacamera/latest.weights")
# DARKNET_DATASET_FILE = os.path.join(DARKNET_PATH, "manacamera/dataset.txt")

DARKNET_LABEL_FILE = os.path.join(DARKNET_PATH, "manacamera/labels.txt")
DARKNET_CONFIG_FILE = os.path.join(DARKNET_PATH, "cfg/yolov3-tiny.cfg")
DARKNET_WEIGHT_FILE = os.path.join(DARKNET_PATH, "yolov3-tiny.weights")
DARKNET_DATASET_FILE = os.path.join(DARKNET_PATH, "cfg/coco.data")