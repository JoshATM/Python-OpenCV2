import os
import cv2 # pip install opencv-python

capture = cv2.VideoCapture(0)
detail = .1 # detail of ascii art (0.1 - 1)
ScreenX = round(detail*capture.get(cv2.CAP_PROP_FRAME_WIDTH))
ScreenY = round(detail*capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

def row_to_ascii(row):
    order = (' ', '.', "'", ',', ':', ';', 'c', 'l', 'x', 'o', 'k', 'X', 'd', 'O', '0', 'K', 'N')
    return tuple(order[int(x / (255 / 16))] for x in row)[::-1] # convert each pixel to ascii

def whole_to_ascii(inFrame):
    return tuple(row_to_ascii(row) for row in inFrame) # convert each row to ascii

while cv2.waitKey(1):
    ret, frame = capture.read() # get each frame
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # colour frame to grey
    
    newFrame = cv2.resize(grayFrame, (int(ScreenX), int(ScreenY))) # resize frame to fit screen
    
    finalFrame = whole_to_ascii(newFrame) # convert frame to ascii
    os.system("clear") # clear screen
    print("\n".join((''.join(row) for row in finalFrame)), end='') # print frame
    
    cv2.imshow('frame', newFrame) # show frame