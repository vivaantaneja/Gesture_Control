## Problem statement

To validate a hand tracking module that can detect and track the movements of the hand in real-time and recognize specific hand gestures for controlling electronic devices or applications.

## Description of problem

The hand-tracking gesture control project aims to allow users to control the volume of their laptops by simply adjusting their fingers. This project will utilize a webcam or a depth camera to track the movement and position of the user's hand and fingers. The system will then interpret the hand gestures to adjust the laptop's volume. The system will be built using Python programming language and OpenCV computer vision library. OpenCV provides a variety of tools for image processing, including hand and gesture recognition. The system will use the Haar cascade classifier algorithm to detect the user's hand in the video feed from the webcam. Once the user's hand is detected, the system will use computer vision techniques to track the movement and position of the user's fingers. The project will use a pre-trained deep learning model, such as Convolutional Neural Networks (CNNs), to recognize different hand gestures. The system will interpret the user's hand gestures to adjust the laptop's volume. For example, extending the thumb up and the index finger down could increase the volume, while the opposite motion could decrease the volume. The project can be tested on a Windows or macOS operating system laptop. The final system will be an application that runs in the background and detects hand gestures from the webcam feed. The application will then send commands to the operating system to adjust the volume of the laptop. Overall, this project will provide a convenient and hands-free way for users to control the volume of their laptops. It will demonstrate the capabilities of computer vision and deep learning in creating intuitive and interactive user interfaces.
At the end of our project, to analyze the reviews, we used sentiment analysis. Sentiment analysis is one of many tasks that AI agents can perform. AI agents can be programmed to perform various tasks, such as natural language processing, speech recognition, image recognition, decision-making, and many more. 


## Code and Explanation 

You need to install certain modules and libraries in your system before implementing the source code. Here is the list of this modules along with their documentations:
•	OpenCV: https://opencv.org 
•	MediaPipe: https://developers.google.com/mediapipe 
•	"MediaPipe Hands: On-device Real-time Hand Tracking" by Valentin Bazarevsky et al. (2020): https://arxiv.org/abs/2006.10214 
•	Python's time module: https://docs.python.org/3/library/time.html 
•	NumPy: https://numpy.org/doc/stable/
•	ctypes: https://docs.python.org/3/library/ctypes.html 
•	comtypes: https://pythonhosted.org/comtypes/ 
•	pycaw: https://github.com/AndreMiras/pycaw/  
•	TextBlob: https://textblob.readthedocs.io/en/dev/ 

handTrackingModule.py:

This code is a Python script that uses the OpenCV and MediaPipe libraries to detect and track hands in real-time video captured by a camera. It defines a handDetector class that initializes the MediaPipe Hands module, which uses a pre-trained machine learning model to detect and track the location of hands in an image. The class contains methods to find hands in an image and to find the positions of landmarks on a detected hand. The main() function creates an instance of the handDetector class and uses it to process the video stream from the camera, displaying the video and the landmarks detected on the hand in real-time. Additionally, it displays the frames per second (FPS) of the processed video. This code is important as it demonstrates how machine learning can be used to detect and track objects in real-time, opening up many potential applications in fields such as robotics, computer vision, and human-computer interaction.

VolumeControl.py:

This code is an example of using gesture control AI to control the volume of a computer using hand gestures detected by a webcam. The code imports the necessary libraries, including OpenCV for image processing, numpy for numerical operations, and a custom handTrackingModule that uses the MediaPipe library to detect and track hand landmarks in real-time. The code initializes the webcam and audio devices and sets the minimum and maximum volume values. It then enters a loop where it reads frames from the webcam, processes them using the handTrackingModule to detect hand landmarks, and calculates the distance between two specific landmarks on the hand to determine the desired volume level. The volume level is then set using the pycaw library, and a visual representation of the volume level is displayed on the screen as a vertical bar. The code also displays the FPS of the webcam feed and updates the display continuously. 

sentimentanalysis.py:

This is a Python code snippet that uses the TextBlob library to analyze the sentiment of a given sentence. The code defines a function called get_sentiment which takes a sentence as input and returns the sentiment of the sentence as either "positive", "negative", or "neutral". The function first creates a TextBlob object with the input sentence. Then, it uses the sentiment property of the TextBlob object to get the polarity score of the sentence. The polarity score ranges from -1 to 1, with -1 indicating a very negative sentiment and 1 indicating a very positive sentiment. Based on the polarity score, the function classifies the sentiment as positive if the polarity score is greater than 0, negative if it is less than 0, or neutral if it is exactly 0. Finally, the function returns the sentiment. The code also includes an example usage, where the user is prompted to enter a sentence and the get_sentiment function is called on that sentence to determine its sentiment. The sentiment is then printed to the console.



