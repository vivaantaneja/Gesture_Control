import cv2  # import the OpenCV library for computer vision tasks
import mediapipe as mp  # import the Mediapipe library for hand tracking
import time  # import the time module for measuring execution time

class handDetector():  # create a class for hand detection
    def __init__(self,mode=False, maxHands = 2, modelComplexity=1,
                 detectionCon = 0.5, trackCon = 0.5):  # define the class constructor with default parameters
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        # initialize the hand detection module and drawing utilities from Mediapipe library
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.modelComplexity,
                                        self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img, draw=True):  # define a method for finding hands in an image
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # convert the input image from BGR format to RGB format
        self.results = self.hands.process(imgRGB)  # process the image using the hand detection module
        if self.results.multi_hand_landmarks:  # check if hand landmarks are detected in the image
            for self.handLms in self.results.multi_hand_landmarks:  # iterate over the detected hand landmarks
                if draw:
                    # draw the landmarks and connections on the input image using the drawing utilities
                    self.mpDraw.draw_landmarks(img, self.handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self,img, handNo = 0):  # define a method for finding the position of hand landmarks in an image

        lmList = []  # create an empty list for storing landmark positions
        if self.results.multi_hand_landmarks:  # check if hand landmarks are detected in the image
            myHand = self.results.multi_hand_landmarks[handNo]  # get the landmarks of the specified hand
            for id, lm in enumerate(myHand.landmark):  # iterate over the landmarks of the hand
                h, w, c = img.shape  # get the height, width, and number of channels of the input image
                cx, cy = int(lm.x * w), int(lm.y * h)  # calculate the pixel coordinates of the landmark
                lmList.append([id, cx, cy])  # add the landmark ID and pixel coordinates to the list

        return lmList  # return the list of landmark positions

def main():  # define the main function
    pTime = 0  # initialize the previous time variable for measuring execution time
    cTime = 0  # initialize the current time variable for measuring execution time
    cap = cv2.VideoCapture(0)  # create a VideoCapture object for capturing video from the default camera
    detector= handDetector()  # create an instance of the handDetector class
    while True:  # loop until the user presses a key to quit
        success, img = cap.read()  # read a frame from the video capture
        img = detector.findHands(img)  # find hands in the frame using the handDetector object
        lmList = detector.findPosition(img)  # get the positions of the hand landmarks in the frame
        if len(lmList) != 0: # check if any hand landmarks are detected in the frame
			print(lmList[4]) # print the position of the landmark with ID 4 (the tip of the index finger)
		    cTime = time.time()  # get the current time for measuring execution time
	    fps = 1 / (cTime - pTime)  # calculate the frame rate
	    pTime = cTime  # update the previous time variable for measuring execution time

	    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)  # display the frame rate on the image

	    cv2.imshow("Image", img)  # display the image
	    cv2.waitKey(1)  # wait for a key event, and exit the loop if any key is pressed
if name == "main": # check if the script is being run directly, not imported as a module
	main() # call the main function to start the application
