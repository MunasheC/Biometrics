import face_recognition
import cv2
import numpy as np
import os
import urllib.request
import requests

class FaceRecognition:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Load sample pictures and learn how to recognize them
        saved_faces_dir = "saved faces"
        for filename in os.listdir(saved_faces_dir):
            if filename.endswith(".jpeg") or filename.endswith(".jpg"):
                image_path = os.path.join(saved_faces_dir, filename)
                image = face_recognition.load_image_file(image_path)
                face_encodings = face_recognition.face_encodings(image)
                if len(face_encodings) > 0:
                    encoding = face_encodings[0]
                    self.known_face_encodings.append(encoding)
                    self.known_face_names.append(os.path.splitext(filename)[0])

        # Initialize variables
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

    def detect_faces(self, url, esp32_ip):
        # Get a reference to webcam #0 (the default one)
        # video_capture = cv2.VideoCapture(0)
        

        while True:
            # Grab a single frame of video
            # ret, frame = video_capture.read()
            img_resp = urllib.request.urlopen(url)
            imgnp_arr=np.array(bytearray(img_resp.read()),dtype=np.uint8)
            frame = cv2.imdecode(imgnp_arr, -1)

            if self.process_this_frame:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # Convert the image from BGR color to RGB color
                rgb_small_frame = small_frame[:, :, ::-1]

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = small_frame[:, :, ::-1]
                code = cv2.COLOR_BGR2RGB

                rgb_small_frame = cv2.cvtColor(small_frame, code)

                # Find all the faces and face encodings in the frame of video
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                self.face_names = []

                for face_encoding in self.face_encodings:
                    # Compare faces with known face encodings
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"

                    # Find the best match
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]

                    self.face_names.append(name)

            self.process_this_frame = not self.process_this_frame

            # Loop through each face in this frame of video
            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                # Scale back up face locations since the frame was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                
                requests.get(f'http://{esp32_ip}/attendance?name={name}')

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        # video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    face_rec = FaceRecognition()
    face_rec.detect_faces(url='http://192.168.100.45/cam-mid.jpg', esp32_ip='192.168.100.45')
