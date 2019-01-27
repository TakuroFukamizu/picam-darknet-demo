# -*- coding: utf-8 -*-

import os
from bottle import Bottle, HTTPResponse, response
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
    try:
        image_path = capture()
        response.content_type = 'image/jpeg'
        with open(image_path, 'rb') as fh:
            content = fh.read()
        os.remove(image_path)
        response.set_header('Content-Length', str(len(content)))
        return content
    except Exception as ex:
        print(ex)
        return HTTPResponse(status=500)