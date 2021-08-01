import numpy as np
from numpy.core.arrayprint import dtype_short_repr

import utils.plotImages as plotHelper

import cv2 


original = cv2.imread('./imgs/car-with-np-1.jpg')
copy = original.copy()

#Method 1
mask1 = copy[:,:,0]
mask1[:,:] = 0

#Method 2
mask2 = np.ones_like(original)

#Method 3
mask3 = np.ones(original.shape[:2],dtype=original.dtype)

roi = original.copy()[276:313,288:446]

cv2.imshow('mask1',mask1)
cv2.imshow('mask2',mask2)
cv2.imshow('mask3',mask3)

blured = cv2.blur(roi,(9,9))
original[276:313,288:446] = blured
cv2.imshow('test',original)

plotHelper.addImage(original)
plotHelper.addImage(roi)
plotHelper.showImages(1)


cv2.waitKey()


cv2.destroyAllWindows()