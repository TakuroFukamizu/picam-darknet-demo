# -*- coding: utf-8 -*-

import os
import base64
from io import BytesIO
from bottle import Bottle, HTTPResponse, response, request
from PIL import Image
from .camera import capture

app = Bottle()

@app.hook('after_request')
def after_request():
    # CORS settings
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@app.route('/api/v1/get_preview', method='GET')
def api_ger_preview():
    mode = request.query.get('mode') # file, base64
    mode = 'file' if mode is None else mode
    try:
        image_path = capture()
        content = None
        if mode == 'base64':
            response.content_type = 'text/plain'
            image = Image.open(image_path)
            buffered = BytesIO()
            image.save(buffered, format="JPEG")
            content = base64.b64encode(buffered.getvalue())
        else:
            response.content_type = 'image/jpeg'
            with open(image_path, 'rb') as fh:
                content = fh.read()
        os.remove(image_path)
        response.set_header('Content-Length', str(len(content)))
        return content
    except Exception as ex:
        print(ex)
        return HTTPResponse(status=500)