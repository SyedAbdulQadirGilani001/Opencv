import cv2 as cv
import numpy as np
# coordinates image
def f_cord(event,x,y,flags,params):
    if event==cv.EVENT_LBUTTONDOWN:
        print(x,y)
        cv.circle(img,(x,y),5,(0,0,255),-1)
        cv.imshow('img',img)
# read image
img=cv.imread('29.jpg')
cv.namedWindow('img')
cv.setMouseCallback('img',f_cord)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
f_cord(cv.EVENT_LBUTTONDOWN,0,0,0,0)