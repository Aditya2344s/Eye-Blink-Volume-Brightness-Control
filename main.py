from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
from math import hypot
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
from scipy.spatial import distance
from imutils import face_utils
import dlib

app = Flask(__name__)

# Setup MediaPipe, pycaw, and dlib
mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.75)
mpDraw = mp.solutions.drawing_utils
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volMin, volMax = volume.GetVolumeRange()[:2]

# Setup Eye Blink Detection (dlib)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('Aditya_face_landmarks.dat')

# Initialize webcam
cap = cv2.VideoCapture(0)

# Function to calculate Eye Aspect Ratio (EAR)
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Initialize blink count and total blinks
count = 0
total_blinks = 0
last_blink_time = 0

def generate_frames():
    global count, total_blinks, last_blink_time
    
    while True:
        success, img = cap.read()
        if not success:
            break
        
        img = cv2.flip(img, 1)  # Flip the image horizontally for a mirror view
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = detector(imgGray)

        for face in faces:
            landmarks = predictor(imgGray, face)
            landmarks = face_utils.shape_to_np(landmarks)
            left_eye = landmarks[42:48]
            right_eye = landmarks[36:42]

            # Calculate EAR for both eyes
            left_eye_ear = eye_aspect_ratio(left_eye)
            right_eye_ear = eye_aspect_ratio(right_eye)
            eye_aspect = (left_eye_ear + right_eye_ear) / 2.0

            # Check if eyes are closed (blink detected)
            if eye_aspect < 0.3:
                count += 1
            else:
                if count >= 3:
                    total_blinks += 1  # Increment total blink count after detecting a blink
                count = 0  # Reset count
        
        # Hand Gesture Processing (Brightness and Volume Control)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        left_lmList, right_lmList = [], []

        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_index, hand_landmarks in enumerate(results.multi_hand_landmarks):
                label = results.multi_handedness[hand_index].classification[0].label
                lmList = []
                for lm in hand_landmarks.landmark:
                    h, w, _ = img.shape
                    lmList.append([int(lm.x * w), int(lm.y * h)])
                if label == 'Left':
                    left_lmList = lmList
                elif label == 'Right':
                    right_lmList = lmList
                mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)

        # Brightness control with left hand
        if left_lmList:
            x1, y1 = left_lmList[4]
            x2, y2 = left_lmList[8]
            length = hypot(x2 - x1, y2 - y1)
            bright = np.interp(length, [15, 200], [0, 100])
            sbc.set_brightness(int(bright))

        # Volume control with right hand
        if right_lmList:
            x1, y1 = right_lmList[4]
            x2, y2 = right_lmList[8]
            length = hypot(x2 - x1, y2 - y1)
            vol = np.interp(length, [15, 200], [volMin, volMax])
            volume.SetMasterVolumeLevel(vol, None)

        # Display the blink count
        cv2.putText(img, f"Blink Count: {total_blinks}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Encode image to JPEG format
        _, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        
        # Yield the image for video feed
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
