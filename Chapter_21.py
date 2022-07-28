import cv2 as cv
import numpy as np
def slider():
    pass
img=cv.imread('29.jpg')
path='D:/pictures/'
cv.namedWindow('image')
cv.resizeWindow('image',640,480)
cv.createTrackbar('H','image',0,179,slider)
cv.createTrackbar('S','image',0,255,slider)
cv.createTrackbar('V','image',0,255,slider)
while(1):
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    h=cv.getTrackbarPos('H','image')
    s=cv.getTrackbarPos('S','image')
    v=cv.getTrackbarPos('V','image')
    lower_blue=np.array([h,s,v])
    upper_blue=np.array([180,255,255])
    mask=cv.inRange(hsv,lower_blue,upper_blue)
    result=cv.bitwise_and(img,img,mask=mask)
    cv.imshow('image',result)
    k=cv.waitKey(1)&0xFF
    if k==27:
        break
cv.destroyAllWindows()
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow('image',mask)