#water shaded

#Harris Corner Detection
#Shi-Tomasi 

import cv2
import numpy as np
import matplotlib.pyplot as plot

#template matching
fileName = 'chessboard.jpg';
get_corners_subpixel(fileName)

full = cv2.imread('chessboard.jpg')

corner_detect(full);

full_gray = cv2.cvtColor(full,cv2.COLOR_BGR2GRAY)

full_gray = np.float32(full_gray)

dst = cv2.cornerHarris(full_gray,2,3,0.04,)

dist = cv2.dilate(dst,None)


print(dist.max())	
tenpercentofmax = 0.01* dist.max();
corners =  dist[dist > tenpercentofmax];
print('-------------------')
print(corners.shape)
fullCopy = full.copy();
fullCopy = fullCopy.astype(int);

fullCopy[dist > tenpercentofmax] = 900;

print('-------------------===')
c = np.argwhere(fullCopy == 900 );
print(c.shape)

a = cv2.imread('6coins.jpg')
b = cv2.imread('7coins.jpg',)


plot.subplot(131)
plot.imshow(full)
plot.subplot(132)
plot.imshow(full_gray,cmap='gray')
plot.subplot(133)
plot.imshow(fullCopy,cmap='gray')


plot.show();
#plot.imshow(clip)
#plot.show();


