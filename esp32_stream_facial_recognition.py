import cv2
import urllib.request
import numpy as np
import time
from face_identifier import FaceRecognition

url = 'http://192.168.100.45/cam-mid.jpg'
esp32_ip = '192.168.100.45'

face_rec = FaceRecognition()
face_rec.detect_faces(url, esp32_ip)

