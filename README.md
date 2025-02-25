# Hand Tracking and Gesture Recognition for Touchless UI

## Project Overview

This project is an innovative implementation that combines computer vision and machine learning techniques to control a laptop's mouse cursor and perform click actions using hand gestures. The primary goal is to enhance user interaction with computers through a touchless interface, making it more intuitive and accessible.

## Key Features

- **Real-time Hand Tracking:** Utilizes the MediaPipe library to detect and track hand landmarks in real-time.
- **Gesture Recognition:** Recognizes different hand poses to distinguish between various gestures.
- **Mouse Control:** Maps hand gestures to mouse actions such as cursor movement and clicks using `pyautogui`.
- **Seamless Integration:** Provides a smooth and responsive user experience by integrating real-time video processing with system controls.

## Technologies Used

- **Python:** The primary programming language used for the project.
- **OpenCV:** Utilized for real-time video capture and processing.
- **MediaPipe:** Employed for hand tracking and landmark detection.
- **pyautogui:** Used to control the mouse cursor and perform click actions.
- **NumPy:** Utilized for numerical operations and calculations.

## How It Works

1. **Hand Tracking and Position Detection:** 
   - The `handDetector` class processes the video frames to detect hands and landmarks using MediaPipe.
   - `findHands()` detects hands in the frame.
   - `findPosition()` finds the landmarks of the detected hands.
   - `fingersUp()` checks which fingers are up based on the landmarks.

2. **Mouse Control:**
   - `pyautogui` is used to move the mouse and perform clicks.
   - The screen size is obtained using `pyautogui.size()`.
   - The cursor position is updated smoothly using interpolation.
   - If only the index finger is up, the cursor moves.
   - If both the index and middle fingers are up and close together, a click is performed.

3. **Main Loop:**
   - The video feed is captured and processed.
   - Hand landmarks are detected and used to control the mouse.
   - The frame rate is displayed on the video feed.
   - The loop breaks if the 'q' key is pressed.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/adhi1702/Hand-Tracking-and-Gesture-Recognition-for-Touchless-UI.git
   cd Hand-Tracking-and-Gesture-Recognition-for-Touchless-UI
   ```

2. Install the required libraries:
   ```sh
   pip install opencv-python mediapipe pyautogui numpy
   ```

## Usage

Use hand gestures to control the mouse cursor and perform click actions:
   - Move the cursor by raising your index finger.
   - Perform a click by raising both the index and middle fingers and bringing them close together.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact me:

- LinkedIn: [Adhithyaa Sabareeswaran](https://www.linkedin.com/in/adhithyaa-s/)
- GitHub: [adhi1702](https://github.com/adhi1702)
