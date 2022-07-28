import cv2 as cv
import numpy as np
img=cv.imread('29.jpg')
# horizontal stack
img1=np.hstack((img,img))
cv.imshow('img1',img1)
# vertical stack
img2=np.vstack((img,img))
img2.resize((500,500))
cv.imshow('img2',img2)
cv.waitKey(0)
cv.destroyAllWindows()