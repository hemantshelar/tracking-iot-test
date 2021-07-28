import matplotlib.pyplot as plt
import cv2
import utils.plotImages as pltHelper
import numpy as np

#import color mappings.
from matplotlib import cm


def FindCounters(img):
	c,h= cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
	return c;

def mouseCallBack(event,x,y,flags,param):
	#print('mouse down')
	global marks_updated
	if event == cv2.EVENT_RBUTTONDBLCLK:
		mouseClicked = True;
	if event == cv2.EVENT_LBUTTONDOWN:
		#MARKERS PASSED TO THE WATERHED ALGO
		cv2.circle(marker_image,(x,y),10,current_marker,-1)
		cv2.circle(road_copy,(x,y),10,colors[current_marker],-1)
		marks_updated = True

# R G B and Alpha
def Create_Rgb(index):
	x = cm.tab10(index);
	x = x[:3]
	x = np.array(x)
	x = x * 255
	x = tuple(x)
	return x;


#road = cv2.imread('./imgs/water-bucket.jpg')
road = cv2.imread('./imgs/tomato-bucket.jpg')
#road = cv2.imread('./imgs/tomato-bucket-1.jpg')
#road = cv2.imread('./imgs/soil-1.jpg');
#road = cv2.imread('./imgs/banana-bucket-1.jpg');
#road = cv2.imread('./imgs/green-apples-1.jpg');
#road = cv2.resize(road,(0,0),None,1/5,1/5)
road_copy = road.copy();

marker_image = np.zeros(road.shape[:2],np.int32)
segments = np.zeros(road.shape,np.uint8)

colors = []

for i in range(10):
	colors.append(Create_Rgb(i));

# GLOBAL VARIABLES
n_markders = 10
current_marker = 1
marks_updated = False

cv2.namedWindow('Road Window')
cv2.setMouseCallback('Road Window',mouseCallBack)

while True:
	cv2.imshow('Watershed SEgments',segments)
	cv2.imshow('Road Window',road_copy)

	keyPressed = cv2.waitKey(1)
	if keyPressed == ord('q'):
		break;
	elif keyPressed == ord('c'):
		road_copy = road.copy();
		marker_image = np.zeros(road.shape[:2],np.uint32)
		segments = np.zeros(road.shape,np.uint8)
	elif keyPressed > 0 and chr(keyPressed).isdigit():
		current_marker = int(chr(keyPressed))
	
	if marks_updated:
		marker_image_copy = marker_image.copy()
		cv2.watershed(road,marker_image_copy)
		segments = np.zeros(road.shape,np.uint8)
		
		for color_ind in range(n_markders):
			segments[marker_image_copy== color_ind] = colors[color_ind]


cv2.destroyAllWindows();

segments[segments == colors[1]] = 0
segments[segments != 0] = 255
#segments[marker_image_copy != colors[1]] = 0

gray = cv2.cvtColor(segments,cv2.COLOR_BGR2GRAY);
ret,thresh1 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernal = np.ones((3,3),np.uint8)
dil = cv2.dilate(thresh1,kernel=kernal,iterations=2)


result = FindCounters(dil);
print(len(result));
cv2.drawContours(road,result,None,(0,255,255),4)

cv2.imshow('xxx',road);

cv2.waitKey() ;

#pltHelper.addImage(road_copy)
#pltHelper.addImage(marker_image)
#pltHelper.addImage(segments)
#pltHelper.showImages(2)


cv2.destroyAllWindows();
