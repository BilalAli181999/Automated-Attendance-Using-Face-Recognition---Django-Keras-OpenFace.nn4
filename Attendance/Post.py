import requests
import time

# initialize the Keras REST API endpoint URL along with the input
# image path
KERAS_REST_API_URL = "http://127.0.0.1:8000/MarkAttendance"

# load the input image and construct the payload for the request
for i in (16,23,30):
    
    payload = {"labels": 'bcsf16a0'+str(i)}
    time.sleep(5)
# submit the request
    r = requests.post(KERAS_REST_API_URL, data=payload)
   
# ensure the request was successful
    