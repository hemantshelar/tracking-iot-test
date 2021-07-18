#water shade manual

import numpy as np
import cv2
import matplotlib.pyplot as plot

def showimg(img):
	result = None
	if len(img.shape) > 2:
		result = cv2.cvtColor(img,cv2.COLOR_BGR2RGB);
		plot.imshow(result);
	else:
		plot.imshow(img,cmap='gray')

#read images
coins = cv2.imread('6coinsWhiteBG.jpg');

#Apply Blur 
#blur = cv2.medianBlur(coins,31)

#Convert to gray
coinGray = cv2.cvtColor(coins,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(coinGray,182,255,cv2.THRESH_BINARY)

#noise removal
ksize = 15
kernal = np.ones((ksize,ksize),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernal,2);
ksize = 3;

#distance transformation
#dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5);


#ret , sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

erd = cv2.erode(opening,kernal,iterations=2)

dil = cv2.dilate(erd,kernel=kernal,iterations=2)


#cv2.circle(coins,(2000,500),5,(255,0,0),6)
plot.subplot(121)
showimg(thresh)

plot.subplot(122)
showimg(dil)


plot.show();