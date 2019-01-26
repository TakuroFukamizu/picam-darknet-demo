import os
from bottle import route
from camera import capture
 
@app.route('/add')
def add():
    return ("<h3>Hello World</h3>")

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