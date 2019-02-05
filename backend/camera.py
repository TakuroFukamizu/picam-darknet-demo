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
        # camera.resolution = (1024, 768) # XGA
        camera.resolution = (1024, 1024) # XGA
        camera.vflip = True
        camera.hflip = True
        # sleep(5) # it's need
        sleep(1)
        camera.capture(file_path)
    sleep(2)
    return file_path