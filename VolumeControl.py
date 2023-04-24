# Import necessary libraries
import cv2  # Library for image processing
import time  # Library for time operations
import numpy as np  # Library for numerical operations
import handTrackingModule as htm  # User-defined module for hand tracking
import math  # Library for mathematical operations
from ctypes import cast, POINTER  # Libraries for type casting
from comtypes import CLSCTX_ALL  # Library for creating COM objects
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume  # Library for audio operations

# Set camera dimensions
wCam, hCam = 648, 480

# Access camera input
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Initialize variables
pTime = 0

# Get audio devices and initialize audio control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volrange = volume.GetVolumeRange()
minVol = volrange[0]
maxVol = volrange[1]

# Create hand detector object
detector = htm.handDetector(detectionCon=0.7)

# Set initial values for volume bar and volume
volBar = 400
vol = 0

# Start loop for video processing
while True:
    # Read camera input
    success, img = cap.read()
    
    # Find and display hands in the image
    img = detector.findHands(img)
    
    # Find the positions of landmarks in the hand
    lmList = detector.findPosition(img)
    
    # If landmarks are detected, calculate hand range and adjust volume
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1,y1), 11, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 11, (255,0,255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 3)
        cv2.circle(img, (cx, cy), 11, (255,0,255), cv2.FILLED)

        length = math.hypot(x2-x1,y2-y1)

        # Convert hand range to volume range
        vol = np.interp(length, [20,150], [minVol,maxVol])
        volBar = np.interp(length, [20, 150], [400, 150])

        # Set volume to the calculated value
        volume.SetMasterVolumeLevel(vol, None)

        # Indicate if hand is too close or too far from camera
        if length < 20:
            cv2.circle(img, (cx, cy), 11, (255, 255, 255), cv2.FILLED)
        if length > 150:
            cv2.circle(img, (cx, cy), 11, (255, 255, 0), cv2.FILLED)

    # Draw volume bar on image
    cv2.rectangle(img, (50,150), (85,400), (0,0,0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400),(0, 0, 155), cv2.FILLED)
    cTime = time.time()  # get the current time
    fps = 1/(cTime- pTime)  # calculate the frames per second
    pTime= cTime  # set previous time to current time for the next iteration

    cv2.putText(img,f'FPS: {int(fps)}',(40,50),  # put text on the image with the fps value
                cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)  # set font, size, color, and thickness for the text

    cv2.imshow("Img", img)  # show the image in a window
    cv2.waitKey(1)  # wait for a key event (1 millisecond) to exit the window

