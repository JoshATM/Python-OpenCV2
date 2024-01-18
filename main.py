import os
import cv2 # pip install opencv-python

capture = cv2.VideoCapture(0)
detail = 1
ScreenX = round(detail*capture.get(cv2.CAP_PROP_FRAME_WIDTH))
ScreenY = round(detail*capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

def row_to_ascii(row):
    order = (' ', '.', "'", ',', ':', ';', 'c', 'l', 'x', 'o', 'k', 'X', 'd', 'O', '0', 'K', 'N')
    return tuple(order[int(x / (255 / 16))] for x in row)[::-1]

def whole_to_ascii(inFrame):
    return tuple(row_to_ascii(row) for row in inFrame)

while cv2.waitKey(1):
    ret, frame = capture.read()
    greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # colour frame to grey
    
    newFrame = cv2.resize(greyFrame, (int(ScreenX), int(ScreenY))) # resize frame to fit screen
    
    cv2.imshow('frame')