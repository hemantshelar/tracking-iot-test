import cv2
import numpy as np


def resizeImages(img,x,y):
	resized = cv2.resize(img,(0,0),None,x,y)
	return resized


aru = cv2.imread('../imgs/aa.jpg')
hemant = cv2.imread('../imgs/a.jpg')
x = 1/3;
y = 1/3;
aru = resizeImages(aru,x,y)
x = 1/4;
y = 1/4;
hemant = resizeImages(hemant,x,y)

print(aru.shape)


#cv2.imshow('Aru',aru)
#cv2.imshow('Hemant',hemant)
cv2.imshow('Result',aru)

roi = aru[340:1100,400:650,:]
cv2.imshow('ROI',roi)

cv2.waitKey();
cv2.destroyAllWindows();