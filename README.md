# README.md
✋ Virtual Pinch-and-Drop Using Hand Tracking

A real-time hand tracking project using OpenCV and MediaPipe to detect pinch gestures and move virtual objects.

🚀 Features
	•	Detects pinch gestures using index and thumb tips
	•	Enables drag-and-drop functionality for virtual objects
	•	Uses MediaPipe Hands for efficient real-time tracking
	•	Supports multiple interactive boxes

📌 Requirements

Make sure you have the following dependencies installed:

pip install opencv-python mediapipe numpy

🔧 Installation & Usage
	1.	Clone this repository:

git clone https://github.com/yourusername/Virtual-Pinch-and-Drop.git
cd Virtual-Pinch-and-Drop


	2.	Run the script:

python hand_tracking.py

🖥️ Code Explanation
	•	Uses OpenCV for video capturing and rendering
	•	MediaPipe Hands detects hand landmarks in real-time
	•	Calculates distance between thumb and index for pinch detection
	•	Moves objects when the user pinches and drags them

🎥 Demo

(Upload a short demo video/GIF and add the link here)

🛠️ Future Improvements
	•	Add gesture-based resizing & rotation
	•	Implement custom UI elements for better interaction
	•	Optimize for low-light conditions

📜 License

This project is licensed under the MIT License.
