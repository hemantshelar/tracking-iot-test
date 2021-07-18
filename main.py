import cv2;
import numpy as np
import matplotlib.pyplot as plt


blankImage = np.zeros([512,512,3],dtype=np.uint8)
#blankImage = cv2.imread('imgs/a.jpg')
#blankImage = cv2.resize(blankImage,(0,0),None,1/4,1/4)

while True:
	cv2.rectangle(blankImage,pt1=(0,0),pt2=(510,50),color=(0,0,255),thickness=1)

	cv2.circle(blankImage,(250,250),5,(255,0,0),2)
	cv2.circle(blankImage,(250,250),5,(0,0,0),2)
	cv2.imshow('test',blankImage)
	if cv2.waitKey(5) & 0xFF == ord('q'):
		break;

cv2.destroyAllWindows();





