# Eye-Blink-Volume-Brightness-Control

## Project Overview

**Eye-Blink-Volume-Brightness-Control** is a cutting-edge, hands-free multimedia control system designed for improving accessibility and user interaction. This project utilizes **eye blink detection** and **hand gesture recognition** to control system volume and screen brightness in real time. By leveraging advanced libraries such as **dlib**, **MediaPipe**, and **pycaw**, it offers a seamless, intuitive, and modern solution for controlling system multimedia settings without the need for physical contact with any hardware.

Incorporating facial landmark detection, hand gesture recognition, and audio-visual control, this project aims to demonstrate the power of AI-based interaction in enhancing user experience, especially for individuals with limited mobility or those seeking more immersive and efficient multimedia control methods.

## Key Features

- **Eye Blink Detection**:
  - Uses **dlib's facial landmark detection** to track and analyze eye movements.
  - Detects eye blinks based on the **Eye Aspect Ratio (EAR)**, providing a hands-free method to count blinks and interact with the system.

- **Hand Gesture Recognition**:
  - Leverages **MediaPipe**'s advanced hand tracking capabilities for recognizing hand gestures.
  - Controls system **volume** (via **pycaw**) and **brightness** (via **screen_brightness_control**) using **hand distance-based gestures**.
  
- **Real-Time Control**:
  - The system provides real-time interaction through webcam-based input.
  - Users can control their system’s multimedia settings (volume and brightness) without the need for physical buttons, offering a more dynamic and intuitive control method.

- **Cross-Platform Multimedia Control**:
  - **Volume Control**: Adjusts system volume using the **pycaw** library, which is a Python COM interface to the Windows audio control API.
  - **Brightness Control**: Uses **screen_brightness_control**, a Python library that controls screen brightness across different platforms (Windows, Linux, macOS).

## Use Case

The **Eye-Blink-Volume-Brightness-Control** system is highly beneficial in the following real-world applications:
- **Assistive Technology**: Helps users with limited mobility or dexterity to control their multimedia settings effortlessly.
- **Hands-Free Computing**: Ideal for users in environments where touching devices may not be ideal (e.g., during cooking, exercising, or presentations).
- **Accessibility**: Enhances the computing experience for users with disabilities by providing voice-activated or gesture-based interactions with system controls.

## Technologies Used

- **dlib**: A powerful toolkit for face detection, facial landmark detection, and machine learning. It is used here for detecting eye blinks using **Eye Aspect Ratio (EAR)**.
- **MediaPipe**: A Google framework for building multimodal applied machine learning pipelines. It is used for real-time hand tracking and gesture recognition.
- **pycaw**: A Python library for controlling the audio settings on Windows, enabling programmatic volume control.
- **screen_brightness_control**: A cross-platform Python library for controlling the screen brightness based on user gestures.
- **OpenCV**: An open-source computer vision library used for real-time video processing and visual interaction, allowing us to capture and process the video feed from the webcam.
- **Flask**: A lightweight web framework for serving the webcam feed and handling video streaming in a web-based interface.
- **SciPy**: Used for calculating distances between facial landmarks and hand gestures, essential for precise control of volume and brightness.
- **imutils**: A set of convenience functions to simplify OpenCV tasks, such as resizing and rotating images.

## System Architecture

### 1. **Webcam Capture**
   - The system captures a continuous video feed from the webcam using **OpenCV**.
   - The video feed is processed frame by frame to detect and track faces and hand gestures.

### 2. **Eye Blink Detection**
   - The system utilizes **dlib's face detector** to locate faces in the image.
   - **Facial landmarks** are detected, and the **Eye Aspect Ratio (EAR)** is calculated for both eyes.
   - A blink is registered if the EAR falls below a certain threshold, and the blink count is incremented accordingly.

### 3. **Hand Gesture Recognition**
   - Using **MediaPipe's hand tracking module**, the system tracks key hand landmarks.
   - The distance between landmarks (e.g., thumb and index finger) is used to control the **brightness** and **volume**.
   - **Brightness** is adjusted with the left hand, and **volume** is adjusted with the right hand, using a **distance-to-action mapping**.

### 4. **Real-Time Control**
   - The system continuously monitors the hand gestures and adjusts the **system brightness** and **volume** in real time, providing an interactive, hands-free control experience.
   
### 5. **Web Interface (Flask)**
   - The webcam feed is processed and displayed through a **Flask web application**. This allows users to interact with the system directly through their browser.

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/Eye-Blink-Volume-Brightness-Control.git
cd Eye-Blink-Volume-Brightness-Control

Step 2: Install dependencies
You can install the required dependencies via pip by running:

bash
Copy code
pip install -r requirements.txt
Step 3: Download the Facial Landmark Model
The dlib library requires a pre-trained model for facial landmark detection. Download the model from this link and extract it in the project directory.

Step 4: Running the Application
To run the application locally, execute the following command:

bash
Copy code
python app.py
This will start a local server and you can view the application in your browser at http://127.0.0.1:5000/.

Usage
Eye Blink Detection:
The system will continuously detect and count your eye blinks.
The blink count will be displayed on the video feed, helping you track the number of blinks in real time.
Hand Gesture Control:
Left Hand: Controls screen brightness. The distance between the thumb and index finger determines the brightness level.
Right Hand: Controls system volume. The same principle applies, where the distance between hand landmarks adjusts the system volume.
Video Feed Streaming
This project uses Flask to serve the webcam video feed to the browser. The video is processed in real-time, and blink count, volume, and brightness levels are displayed on the live feed.

Video Streaming Endpoint:
URL: /video_feed
MIME Type: multipart/x-mixed-replace
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
We welcome contributions! Feel free to fork the repository and submit pull requests. If you find any bugs or have suggestions for improvement, please open an issue.

Guidelines for Contributions:
Fork the repository.
Create a new branch for your feature or bugfix.
Write clear commit messages.
Submit a pull request.
Acknowledgments
dlib: For providing a robust facial landmark detection model.
MediaPipe: For offering an efficient framework for real-time hand gesture recognition.
pycaw: For enabling easy system volume control on Windows.
screen_brightness_control: For providing cross-platform screen brightness control.
OpenCV: For its powerful video processing capabilities.
Flask: For the simple yet effective web framework.
Screenshots
Real-time video feed showing blink count and hand gestures for control.

System controlling volume and brightness with hand gestures in the video feed.

Contact
For any inquiries or feedback, feel free to reach out via GitHub issues or email at your.email@example.com.

markdown
Copy code

### Additional Details:
1. **Dependencies**: This extended `README.md` provides a technical breakdown of the libraries and how they are integrated into the project.
2. **Detailed Explanation**: It gives an in-depth explanation of each feature, including the methods used for **Eye Blink Detection**, **Hand Gesture Recognition**, and **Real-Time Control**.
3. **System Architecture**: It describes how the entire system works, from video capture to control interaction.
4. **Installation Instructions**: Clear steps to clone the repository, install dependencies, and run the application.
5. **Usage**: A more detailed usage section, explaining how users can interact with the system to control volume and brightness.
6. **Screenshots**: The placeholders for screenshots can be updated once you have images that show the functionality in action.

### How to Add Images:
1. Create an `images` folder in the root of your project repository.
2. Add images such as screenshots of your application in action (e.g., `screenshot1.png`).
3. Reference those images using markdown syntax like `![Screenshot](images/screenshot1.png)`.

This version provides a more detailed and professional approach, s

