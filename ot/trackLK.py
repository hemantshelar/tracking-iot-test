import numpy as np
import cv2
import matplotlib.pyplot as plot

ix,iy,k = 200,200,1
def onMouseClick(event,x,y,flag,param):
	global ix,iy,k
	if event == cv2.EVENT_LBUTTONDOWN:
		ix = x;
		iy = y;
		k = -1;

##############################
nw = "live"
cv2.namedWindow(nw)
cv2.setMouseCallback(nw,onMouseClick)


cap = cv2.VideoCapture(0)
oldPoints = None;
oldGray = None
while True:
	_,frame = cap.read();
	cv2.imshow(nw,frame)
	if cv2.waitKey(5) & 0xFF == ord('q') or k == -1:
		oldPoints = np.array([[ix,iy]],dtype=np.float32).reshape(-1,1,2)
		oldGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		break;


mask = np.zeros_like(frame);

while True:
	_,frame = cap.read();
	newGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	new_pts ,status, err = cv2.calcOpticalFlowPyrLK(oldGray,newGray,oldPoints,None,maxLevel=1,
	criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,15,0.08))

	center = new_pts.ravel();

	maskCopy = mask.copy()

	cv2.circle(maskCopy,(center[0],center[1]),50,(0,255,0),5)

	combined = cv2.addWeighted(frame,0.7,maskCopy,0.3,0.1)

	cv2.imshow(nw,combined)

	oldGray = newGray
	oldPoints = new_pts.copy()

	if cv2.waitKey(5) & 0xFF == ord('q') :
		break;

cap.release();
cv2.destroyAllWindows();