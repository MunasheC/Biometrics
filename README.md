# Biometrics
Enhancing security and facilitating efficient identity verification through a low-cost, effective biometric system.

# Face Recognition with ESP32 Integration

This project demonstrates real-time face recognition using the `face_recognition` library in Python and integrates it with an ESP32 microcontroller for additional functionality.

## Description

The Face Recognition with ESP32 Integration project allows you to perform the following tasks:
- Recognize faces in real-time using a webcam or video stream.
- Display bounding boxes around detected faces and label them with their names.
- Integrate with an ESP32 microcontroller to trigger actions based on recognized faces.

## Features

- Face detection and recognition using the `face_recognition` library.
- Real-time video stream processing for face recognition.
- Integration with an ESP32 microcontroller for external actions.
- Customizable face database for recognition.

## Installation

To run this project, you need to have Python installed on your system. Additionally, ensure you have the necessary libraries installed by running:

```bash
pip install face_recognition opencv-python numpy requests

## Usage

1. Place your face images in the `saved faces` directory.
2. Update the `esp32_ip` variable in the `main()` function of `face_identifier.py` with the IP address of your ESP32 device.
3. Run the `face_identifier.py` script to start face recognition.

```bash
python face_identifier.py

## Configuration

- Face Images: Place images of faces to be recognized in the saved faces directory. Ensure images are clear and well-lit.
- ESP32 Integration: Adjust the IP address of your ESP32 device in the esp32_ip variable to enable integration with the microcontroller.

## Credits

- The `face_recognition` library was developed by Adam Geitgey
- This project was created by Munashe Chihota



