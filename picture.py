import time
import picamera
 
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.vflip = True 
    #camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('my_picture.jpg')

