import matplotlib.pyplot as plt
import cv2
import utils.plotImages as pltHelper
import numpy as np

#import color mappings.
from matplotlib import cm

def FindCounters(img):
	c,h= cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	return c

def mouseCallBack(event,x,y,flags,param):
	#print('mouse down')
	global marks_updated
	if event == cv2.EVENT_RBUTTONDBLCLK:
		mouseClicked = True
	if event == cv2.EVENT_LBUTTONDOWN:
		#MARKERS PASSED TO THE WATERHED ALGO
		cv2.circle(marker_image,(x,y),10,current_marker,-1)
		cv2.circle(original_copy,(x,y),10,colors[current_marker],-1)
		marks_updated = True

# R G B and Alpha
def Create_Rgb(index):
	x = cm.tab10(index);
	x = x[:3]
	x = np.array(x)
	x = x * 255
	x = tuple(x)
	return x


#original = cv2.imread('./imgs/water-bucket.jpg')
original = cv2.imread('./imgs/tomato-bucket.jpg')
#original = cv2.imread('./imgs/tomato-bucket-1.jpg')
#original = cv2.imread('./imgs/soil-1.jpg');
#original = cv2.imread('./imgs/banana-bucket-1.jpg');
#original = cv2.imread('./imgs/green-apples-1.jpg');
#original = cv2.resize(original,(0,0),None,1/5,1/5)
original_copy = original.copy();

marker_image = np.zeros(original.shape[:2],np.int32)
segments = np.zeros(original.shape,np.uint8)

colors = []

for i in range(10):
	colors.append(Create_Rgb(i));

# GLOBAL VARIABLES
nTotalMarkers = 10
current_marker = 1
marks_updated = False

cv2.namedWindow('Main Window')
cv2.setMouseCallback('Main Window',mouseCallBack)

while True:
	cv2.imshow('Watershed SEgments',segments)
	cv2.imshow('Main Window',original_copy)

	keyPressed = cv2.waitKey(1)
	if keyPressed == ord('q'):
		break
	elif keyPressed == ord('c'):
		original_copy = original.copy();
		marker_image = np.zeros(original.shape[:2],np.uint32)
		segments = np.zeros(original.shape,np.uint8)
	elif keyPressed > 0 and chr(keyPressed).isdigit():
		current_marker = int(chr(keyPressed))
	
	if marks_updated:
		marker_image_copy = marker_image.copy()
		cv2.watershed(original,marker_image_copy)
		segments = np.zeros(original.shape,np.uint8)
		
		for color_ind in range(nTotalMarkers):
			segments[marker_image_copy== color_ind] = colors[color_ind]

cv2.destroyAllWindows()

segments[segments == colors[1]] = 0
segments[segments != 0] = 255
#segments[marker_image_copy != colors[1]] = 0

gray = cv2.cvtColor(segments,cv2.COLOR_BGR2GRAY);
ret,thresh1 = cv2.threshold(gray,0,255,cv2.THRESH_OTSU + cv2.THRESH_BINARY)

kernal = np.ones((5,5),np.uint8)
erd = cv2.erode(thresh1,kernel=kernal)
dil = cv2.dilate(erd,kernel=kernal,iterations=2)

cv2.imshow('Dilated Image',dil)

result = FindCounters(dil);


for cnt in result:
	area = cv2.contourArea(cnt)
	if area < 10000:
		cv2.drawContours(original,[cnt],None,(0,255,255),3)
	else:
		cv2.drawContours(original,[cnt],None,(0,0,255),3)

		

#cv2.drawContours(original,result,None,(0,255,255),4)

msg = f'{len(result)}'
cv2.imshow(msg,original);

pltHelper.addImage(original_copy)
#pltHelper.addImage(marker_image)
#pltHelper.addImage(segments)
pltHelper.showImages(2)

cv2.waitKey()

cv2.destroyAllWindows();
