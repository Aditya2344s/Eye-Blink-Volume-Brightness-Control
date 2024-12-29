# Eye-Blink-Volume-Brightness-Control

## Overview

**Eye-Blink-Volume-Brightness-Control** is an innovative hands-free multimedia control system that leverages eye blink detection and hand gestures. This project uses advanced libraries such as **dlib**, **MediaPipe**, and **pycaw** to control system volume and screen brightness with intuitive user gestures. It provides a seamless, real-time interaction experience without the need for physical contact or buttons.

## Features

- **Eye Blink Detection**: Uses **dlib**'s facial landmark detection to track eye movements and detect blinks. Each blink is counted and displayed in real-time.
- **Hand Gesture Recognition**: Leverages **MediaPipe** to recognize hand gestures. Controls include adjusting system volume with the right hand and screen brightness with the left hand.
- **Audio Control**: Volume control is handled using **pycaw**, providing a dynamic adjustment of system volume based on hand gestures.
- **Brightness Control**: Adjusts screen brightness via **screen_brightness_control** based on the distance between hand landmarks.
  
## Requirements

To run this project, you will need to install the following dependencies:

- Python 3.x
- OpenCV
- MediaPipe
- dlib
- pycaw
- screen_brightness_control
- imutils
- scipy

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
