import os
import cv2 # pip install opencv-python

capture = cv2.VideoCapture(0)
detail = 1
ScreenX = round(detail*capture.get(cv2.CAP_PROP_FRAME_WIDTH))
ScreenY = round(detail*capture.get(cv2.CAP_PROP_FRAME_HEIGHT))


while cv2.waitKey(1):
    ret, frame = capture.read()
    greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # colour frame to grey
    
    newFrame = cv2.resize(greyFrame, (int(ScreenX), int(ScreenY))) # resize frame to fit screen
    
    cv2.imshow('frame')