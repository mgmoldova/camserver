
import requests
import json
import cv2

addr = 'http://localhost:5000'
test_url = addr + '/api/test'

# prepare headers for http request
content_type = 'image/png'
headers = {'content-type': content_type}

cap = cv2.VideoCapture(-1)
ret, image_np = cap.read()
cv2.imwrite('foo.png', image_np)
img = cv2.imread('foo.png')
# encode image as jpeg
_, img_encoded = cv2.imencode('.png', img)
# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
# decode response
print(json.loads(response.text))

# expected output: {u'message': u'image received. size=124x124'}