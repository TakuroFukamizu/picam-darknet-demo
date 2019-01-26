# -*- coding: utf-8 -*-

import os
from bottle import Bottle, HTTPResponse, response
from .camera import capture

app = Bottle()

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