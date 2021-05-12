from flask import Flask, request, Response, render_template
import jsonpickle
import numpy as np
import cv2
import os

PEOPLE_FOLDER = os.path.join('static', 'images')
# Initialize the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route("/")
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'test1.png')
    return render_template("index.html", user_image = full_filename)
# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)
    cv2.imwrite("static/images/test1.png", img)
    return Response(response=response_pickled, status=200, mimetype="application/json")


# start flask app
app.run(host="0.0.0.0", port=5000)