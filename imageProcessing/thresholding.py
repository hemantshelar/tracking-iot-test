import numpy as np
import cv2

def resizeImages(img,x,y):
	resized = cv2.resize(img,(0,0),None,x,y)
	return resized

img = cv2.imread('../imgs/aa.jpg',0)
img = resizeImages(img,1/5,1/5)

th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,41,8)

cv2.imshow('img',img)
cv2.imshow('th',th)

cv2.waitKey();

cv2.destroyAllWindows();


#Adaptive threshold