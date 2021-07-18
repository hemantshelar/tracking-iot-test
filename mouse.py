from typing import Tuple
import cv2
import numpy as np

windowName = "BlankWindow"
isDrawing = False
px = -1
py = -1
###########################
##### FUNCTION ############
###########################
def draw_circle(event,x,y,flags,param):
	global isDrawing,px,py;
	
	if event == cv2.EVENT_RBUTTONDOWN:
		#cv2.circle(bi,(x,y),5,(255,0,0),-1)
		isDrawing = True
		print(f'({x},{y})')
	if event == cv2.EVENT_RBUTTONUP:
		isDrawing = False
	if event == cv2.EVENT_MOUSEMOVE:
		if isDrawing == True:
			skipDraw = px == -1;
			px = x;
			py = y;
			if skipDraw == False:	
				cv2.line(bi,(px,py),(x,y),(0,255,0),1)

cv2.namedWindow(windowName);
cv2.setMouseCallback(windowName,draw_circle)

#Create black image
bi = np.zeros((512,512,3),np.uint8)
isDrawing = False

while True:
	cv2.imshow(windowName,bi);
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break;
cv2.destroyAllWindows();