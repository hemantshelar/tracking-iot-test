import cv2
import numpy as np

import matplotlib.pyplot as plot


import utils.plotImages as u;


aru = cv2.imread('imgs/aru.jpg');
aru = cv2.resize(aru,(0,0),None,1/4,1/4)
imgray = cv2.cvtColor(aru,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)

i,c,h = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for cnt in c:
	cv2.drawContours(aru,[cnt],-1,(0,255,0),4);


cv2.imshow("thresh",aru);

while True:	
	if cv2.waitKey(5) & 0xFF == ord('q'):
		break;
cv2.destroyAllWindows(); 