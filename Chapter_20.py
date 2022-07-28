from logging import captureWarnings
import cv2 as cv
import numpy as np
cap=cv.VideoCapture('Ya_Rahmn.mp4')
frame=0
while True:
    success , frame = cap.read()
    if success:
        cv.imwrite('frames.jpg')
    else:
        break
    frame=frame+2
cap.release()