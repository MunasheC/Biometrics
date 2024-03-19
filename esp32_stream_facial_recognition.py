import cv2
import urllib.request
import numpy as np
import time
import requests

# Replace the URL with the IP camera's stream URL
url = 'http://192.168.100.45/cam-lo.jpg'
cv2.namedWindow("live Cam Testing", cv2.WINDOW_AUTOSIZE)
esp32_ip = '192.168.100.45'


# Create a VideoCapture object
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

faces_data = []

# Check if the IP camera stream is opened successfully
if not cap.isOpened():
    print("Failed to open the IP camera stream")
    exit()

# Read and display video frames
while True:
    # Read a frame from the video stream
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    #ret, frame = cap.read()
    im = cv2.imdecode(imgnp,-1)

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x+w, y+h), (255, 0, 0), 5)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = im[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
           cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5) 
        #    print("Hi Munashe. Nice to see you!")
           
           if (requests.get(f'http://{esp32_ip}/led?command=blink')):
                print(requests.get(f'http://{esp32_ip}/led?command=blink'))   
                print("--------->>> Face detected.")
                time.sleep(60)

    cv2.imshow('live Cam Testing',im)
    key=cv2.waitKey(5)
    if key==ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()