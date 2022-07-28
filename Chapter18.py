import cv2 as cv
import numpy as np
img=cv.imread('29.jpg')
# persective transform
pts1=np.float32([[0,0],[0,img.shape[0]],[img.shape[1],0],[img.shape[1],img.shape[0]]])
img_size=img.shape
pts2=np.float32([[0,0],[0,img_size[0]],[img_size[1],0],[img_size[1],img_size[0]]])
M=cv.getPerspectiveTransform(pts1,pts2)
dst=cv.warpPerspective(img,M,(img_size[1],img_size[0]))
cv.imwrite('29_perspective.jpg',dst)
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()