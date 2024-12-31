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


git clone https://github.com/yourusername/Eye-Blink-Volume-Brightness-Control.git
cd Eye-Blink-Volume-Brightness-Control

Certainly! Here’s your markdown updated with proper formatting and headings for **Step 2** and other steps:


# Eye-Blink-Volume-Brightness-Control

### Installation and Setup

### Step 1: Clone the Repository
To begin, clone the repository to your local machine by running the following command:

```bash
git clone https://github.com/yourusername/Eye-Blink-Volume-Brightness-Control.git
cd Eye-Blink-Volume-Brightness-Control
```

### Step 2: Install Dependencies
You can install the required dependencies using `pip` by running:

```bash
pip install -r requirements.txt
```

### Step 3: Download the Facial Landmark Model
The **dlib** library requires a pre-trained model for facial landmark detection. 

### Step 4: Running the Application
To run the application locally, execute the following command:

```bash
python main.py
```

This will start a local server, and you can view the application in your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

### Eye Blink Detection
- The system continuously detects and counts eye blinks in real time.
- The blink count is displayed on the video feed, allowing you to track your blinking behavior.

### Hand Gesture Control
- **Left Hand**: Controls **screen brightness**. The distance between the thumb and index finger determines the brightness level.
- **Right Hand**: Controls **system volume**. The same principle applies to adjust the system volume based on the distance between hand landmarks.

### Video Feed Streaming
This project uses **Flask** to stream the webcam video feed to the browser. The video is processed in real-time, with the blink count, volume, and brightness levels displayed on the live feed.

## License
This project is licensed under the **MIT License**. For more details, refer to the [LICENSE](LICENSE) file.

## Contributing
We welcome contributions! Feel free to fork the repository and submit pull requests. If you encounter any bugs or have suggestions for improvement, please open an issue.

### Contribution Guidelines:
1. **Fork** the repository.
2. **Create** a new branch for your feature or bugfix.
3. **Write clear commit messages** to describe your changes.
4. **Submit** a pull request for review.

## Acknowledgments
- **dlib**: For providing the robust facial landmark detection model.
- **MediaPipe**: For offering an efficient framework for real-time hand gesture recognition.
- **pycaw**: For enabling system volume control on Windows.
- **screen_brightness_control**: For providing cross-platform screen brightness control.
- **OpenCV**: For its powerful video processing capabilities.
- **Flask**: For its lightweight and effective web framework.
## Screenshots

### Demo
![Screenshot 2024-12-31 095549](https://github.com/user-attachments/assets/ad4bdb26-e916-4bfd-b2bf-9b732f4608c2)

### Real-time video feed displaying blink count and hand gestures for control.

https://github.com/user-attachments/assets/e6f6119f-c841-46da-b578-9ded6ce83853



## Contact
For any inquiries or feedback, please feel free to reach out via GitHub issues or email at `singaditya934@gmail.com`.
