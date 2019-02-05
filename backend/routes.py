# -*- coding: utf-8 -*-

import os
import base64
from io import BytesIO
from bottle import Bottle, HTTPResponse, response, request, static_file
from PIL import Image
from .camera import capture
from .configs import ROOT_DIR
from .configs import DARKNET_PATH, DARKNET_CONFIG_FILE, DARKNET_WEIGHT_FILE, DARKNET_DATASET_FILE
from .detector import Detector
from .darknet import YoloConfig


def image_to_base64(image: Image, format="JPEG"):
    buffered = BytesIO()
    image.save(buffered, format=format)
    content = base64.b64encode(buffered.getvalue())
    return content

config = YoloConfig()
config.config_file = DARKNET_CONFIG_FILE
config.weights_file = DARKNET_WEIGHT_FILE
config.dataset_file = DARKNET_DATASET_FILE
    

app = Bottle()

@app.hook('after_request')
def after_request():
    # CORS settings
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@app.route('/api/v1/get_preview', method='GET')
def api_get_preview():
    mode = request.query.get('mode') # file, base64
    mode = 'file' if mode is None else mode
    image_path = None
    try:
        image_path = capture()
        r = None
        if mode == 'base64':
            image = Image.open(image_path)
            body = image_to_base64(image, format="JPEG")

            r = HTTPResponse(status=200, body=body)
            r.set_header('Content-Type', 'text/plain')
        else:
            body = None
            with open(image_path, 'rb') as fh:
                body = fh.read()
            
            r = HTTPResponse(status=200, body=body)
            r.set_header('Content-Type', 'image/jpeg')
        # response.set_header('Content-Length', str(len(content)))
        return r
    except Exception as ex:
        print(ex)
        return HTTPResponse(status=500)
    finally:
        if image_path and os.path.exists(image_path):
            os.remove(image_path)

@app.route('/api/v1/detect_people', method='GET')
def api_detect_people():
    global config
    detector = Detector(config)
    results, result_image, origin_image = detector.run()
    result_image_b64 = image_to_base64(result_image, format="JPEG")
    origin_image_b64 = image_to_base64(origin_image, format="JPEG")

    body = {
        detects: detector,
        result_image: result_image_b64,
        result_image: origin_image_b64
    }
    
    r = HTTPResponse(status=200, body=body)
    r.set_header("Content-Type", "application/json")
    return r

@app.route('/')
def index():
    return static_file('index.html', root=os.path.join(ROOT_DIR, 'dist'))

# serve frontend files
@app.route("/<filepath:path>", name="static_file")
def static(filepath):   
    return static_file(filepath, root=os.path.join(ROOT_DIR, 'dist'))