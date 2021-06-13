from flask import Flask, request, Response, render_template
import jsonpickle
import numpy as np
import cv2
import os
from camera import Camera

PEOPLE_FOLDER = os.path.join('static', 'images')
# Initialize the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
full_filename = [1,2,3,4,5,6,7,8]

@app.route("/")
def index():
    full_filename[0] = os.path.join(app.config['UPLOAD_FOLDER'], 'test1.png')
    full_filename[1] = os.path.join(app.config['UPLOAD_FOLDER'], 'test2.png')
    full_filename[2] = os.path.join(app.config['UPLOAD_FOLDER'], 'test3.png')
    full_filename[3] = os.path.join(app.config['UPLOAD_FOLDER'], 'test4.png')
    full_filename[4] = os.path.join(app.config['UPLOAD_FOLDER'], 'test5.png')
    full_filename[5] = os.path.join(app.config['UPLOAD_FOLDER'], 'test6.png')
    full_filename[6] = os.path.join(app.config['UPLOAD_FOLDER'], 'test7.png')
    full_filename[7] = os.path.join(app.config['UPLOAD_FOLDER'], 'test8.png')
    return render_template("index.html", user_image1 = full_filename[0], user_image2 = full_filename[1], user_image3 = full_filename[2], user_image4 = full_filename[3], user_image5 = full_filename[4], user_image6 = full_filename[5],  user_image = full_filename[6], user_image8 = full_filename[7] )
# route http posts to this method

@app.route('/video')
def video():
    """Video streaming home page."""
    return render_template('video.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_test')
def video_test():
    """Video streaming route. Put this in the src attribute of an img tag."""
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
    cv2.imwrite("1.jpg", img)
    return Response(response=response_pickled, status=200, mimetype="application/json")



@app.route('/api/test/1', methods=['POST'])
def test1():
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

@app.route('/api/test/2', methods=['POST'])
def test2():
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
    cv2.imwrite("static/images/test2.png", img)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/api/test/3', methods=['POST'])
def test3():
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
    cv2.imwrite("static/images/test3.png", img)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/api/test/4', methods=['POST'])
def test4():
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
    cv2.imwrite("static/images/test4.png", img)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/api/test/5', methods=['POST'])
def test5():
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
    cv2.imwrite("static/images/test5.png", img)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/api/test/6', methods=['POST'])
def test6():
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
    cv2.imwrite("static/images/test6.png", img)
    return Response(response=response_pickled, status=200, mimetype="application/json")    

@app.route('/api/test/7', methods=['POST'])
def test7():
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
    cv2.imwrite("static/images/test7.png", img)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/api/test/8', methods=['POST'])
def test8():
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
    cv2.imwrite("static/images/test8.png", img)
    return Response(response=response_pickled, status=200, mimetype="application/json")

if __name__ == '__main__':
    app.run(port="6655")