# -*- coding: utf-8 -*-

import os
from time import sleep
from datetime import datetime
from .configs import TEMP_CAPTURED_DIR

def capture():
    import picamera
    file_name = "{}.jpg".format(datetime.now().strftime("%Y%m%d-%H%M%S"))
    file_path = os.path.join(TEMP_CAPTURED_DIR, file_name)
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768) # XGA
        camera.vflip = True
        sleep(5) # it's need
        camera.capture(file_path)
    return file_path