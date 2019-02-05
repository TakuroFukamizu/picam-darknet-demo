# -*- coding: utf-8 -*-

import os
from PIL import Image
from backend.camera import capture
# from darknet import load_net, load_meta, detect
from backend.darknet import exec_darknet, YoloConfig
from backend.configs import DARKNET_PATH

class Detector:
    _yolo_config = None

    def __init__(self, config: YoloConfig):
        self._yolo_config = config

    def _detect(self, img_path: str):
        # net = load_net(config.config_file, config.weights_file, 0)
        # meta = load_meta(config.dataset_file)
        # r = detect(net, meta, img_path)
        # .so is not working now.
        r = exec_darknet(self._yolo_config, img_path)
        return r
    def _get_detect_image(self):
        result_image_path = os.path.join(DARKNET_PATH, 'detection.jpg')
        result_image = Image.open(result_image_path)
        # os.remove(result_image_path)
        return result_image
    
    def run(self):
        file_path = capture()
        results = self._detect(self._yolo_config, file_path)
        result_image = self._get_detect_image()
        origin_image = Image.open(file_path)
        os.remove(file_path)
        return results, result_image, origin_image

