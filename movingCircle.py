import cv2;
import numpy as np
import matplotlib.pyplot as plt


#blankImage = cv2.imread('imgs/a.jpg')
#blankImage = cv2.resize(blankImage,(0,0),None,1/4,1/4)
#cv2.rectangle(blankImage,pt1=(0,0),pt2=(510,50),color=(0,0,255),thickness=1)

maxX = 512
maxY = 512

curX = 5
curY = 5
r = 5
color = (255,0,0)
thickness = 2

offsetx = 1
offsety = 1


blankImage = np.zeros([maxX,maxY,3],dtype=np.uint8)

cv2.putText(blankImage,"Hello",(50,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,0,0),3,cv2.LINE_4)

while True:
	cv2.circle(blankImage,(curX,curY),r,color,thickness=thickness)
	cv2.imshow('test',blankImage)

	if cv2.waitKey(5) & 0xFF == ord('q'):
		break;
	cv2.circle(blankImage,(curX,curY),r,(0,0,0),thickness=thickness)
	cv2.imshow('test',blankImage)

	curX = curX + offsetx;
	curY = curY + offsety;

	if offsetx == 1:
		if (curX+r > maxX):
			offsetx = -1
	else:
		if ( curX - r <= 0):
			offsetx = 1;
	
	if offsety == 1:
		if ( curY + r > maxY):
			offsety = -1;
	else:
		if ( curY - r <= 0 ):
			offsety = 1;

cv2.destroyAllWindows();




