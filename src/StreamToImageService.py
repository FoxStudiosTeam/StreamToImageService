from flask import *
import requests

app = Flask(__name__)


@app.route('/camera/<id>')
def stream_to_image(id):
    # test
    cameras = requests.get('http://camera-registry-service/get/all').json()
    for camera in cameras:
        if camera["uuid"] == id:
            return requests.get(camera['external_ip'])
        else:
            return Response("", 500)


app.run("0.0.0.0", port=8080, debug=True)
