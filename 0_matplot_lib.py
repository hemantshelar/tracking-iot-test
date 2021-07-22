import matplotlib.pyplot as plt
import cv2
import utils.plotImages as pltHelper
import numpy as np

#import color mappings.
from matplotlib import cm

namedWindow = "window"
mouseClicked = False

current_marker = 1
marks_updated = False


# R G B and alpha
def Create_Rgb(index):
	x = cm.tab10(index);
	x = x[:3]
	x = np.array(x)
	x = x * 255
	x = tuple(x)
	return x;


def onValueChanged(x):
	global mouseClicked;
	mouseClicked = True
def mouseCallBack(event,x,y,flags,param):
	global mouseClicked, marks_updated
	if event == cv2.EVENT_RBUTTONDBLCLK:
		mouseClicked = True;
	if event == cv2.EVENT_LBUTTONDOWN:
		#MARKERS PASSED TO THE WATERHED ALGO
		cv2.circle(marker_image,(x,y),10,(current_marker),-1)
		cv2.circle(marker_image,(x,y),10,(current_marker),-1)
		marks_updated = True
	
blurAmout = 45

cv2.namedWindow(namedWindow)
cv2.resizeWindow(namedWindow, 500,500)
cv2.setMouseCallback(namedWindow,mouseCallBack)
cv2.createTrackbar("ThreshMin",namedWindow,127,255,onValueChanged)

img = cv2.imread('./imgs/cucumbers.jpg')
img = cv2.resize(img,(0,0),None,1/3,1/3)


marker_shape = img.shape[0:2]
marker_image = np.zeros(marker_shape,np.uint32)
segments = np.zeros(img.shape,np.uint8)

print(marker_image.shape)
print(segments.shape)

colors = []
for i in range(10):
	ret = Create_Rgb(i)
	colors.append(ret)

print(colors)


while False:
	if ( mouseClicked == True ):
		print('Processing....')	
		pltHelper.clear();
		mouseClicked = False
		
		rgbImage = cv2.cvtColor(img.copy(),cv2.COLOR_BGR2RGB);
		blur = cv2.medianBlur(img,blurAmout)
		gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)

		minThresh = cv2.getTrackbarPos("ThreshMin",namedWindow)
		ret,thresh = cv2.threshold(gray,minThresh,255,cv2.THRESH_BINARY_INV )
		#noise removal
		kernel = np.ones((3,3),np.uint8)
		opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)

		#distance transform
		dist_tranform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
		print(dist_tranform.shape)


		pltHelper.addImage(img)
		pltHelper.addImage(blur)
		pltHelper.addImage(gray);
		pltHelper.addImage(thresh);
		pltHelper.addImage(opening);
		pltHelper.addImage(dist_tranform);
		pltHelper.showImages(3);

	if ( cv2.waitKey(5) & 0xFF == ord('q')):
		break;


cv2.destroyAllWindows();
