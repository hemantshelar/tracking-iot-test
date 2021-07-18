import cv2
import numpy as np

windowName = 'CCTV';


cap = cv2.VideoCapture(0);
prevFrame = np.zeros((500,640,3),dtype=np.uint8)
cf = None
tf = None

flag = False
dil = np.zeros((500,640,3),dtype=np.uint8)
original = np.zeros((500,640,3),dtype=np.uint8)
thresh = np.zeros((500,640,3),dtype=np.uint8)
diff = np.zeros((500,640,3),dtype=np.uint8)
canny = np.zeros((500,640,3),dtype=np.uint8)

prevFrame = cv2.cvtColor(prevFrame,cv2.COLOR_BGR2GRAY)

lx = 100000000
ly = 100000000
ox = 0
oy = 0

bx = 0
by = 0

maxArea = 0;
minArea = 100000000

gMaxArea = 0;
gMinArea = 100000000

while True:	
	ret,cf = cap.read();
	original = cf.copy();
	cf = cv2.cvtColor(cf,cv2.COLOR_BGR2GRAY)

	if prevFrame.shape[0] == 500:
		flag = False
	else:
		flag = True

	if flag == True:
		diff = cv2.absdiff(prevFrame,cf)
		canny = cv2.Canny(diff,63,108)
		#_,thresh = cv2.threshold(diff,27,150,cv2.THRESH_BINARY)
		dil = cv2.dilate(canny,None,iterations=5)

		imageChanged,counters,h = cv2.findContours(dil.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		print(len(counters))
		try:
			for cnt in counters:
				area = cv2.contourArea(cnt)
				if area > maxArea: 
					maxArea = area
				if area < minArea:
					minArea = area;

				if area > gMaxArea: 
					gMaxArea = area
				if area < gMinArea:
					gMinArea = area;

				x,y,w,h = cv2.boundingRect(cnt);
				if  x < lx:
					lx = x
				if y < ly:
					ly = y;

				print(f"{x},{y},{w},{h}")
				#cv2.rectangle(original,(x,y),(x+w,y+h),(255,0,0),-1)
		except:
			print('error');		

	prevFrame = cf;
	print(f'Max area is {maxArea}')

	if lx == 100000000 or ly == 100000000:
		cv2.circle(original,(ox,oy),10,(0,255,0),5);
	else:
		cv2.circle(original,(lx,ly),10,(0,255,0),5);
		ox = lx
		oy = ly
	cv2.rectangle(original,(ox,oy),(ox+150,oy+150),(255,0,0),5)
	

	cv2.circle(original,(0,0),10,(0,255,0),5);
	cv2.imshow("thresh",original);

	#reset 
	lx = 100000000
	ly = 100000000
	bx = 0
	by = 0
	maxArea = 0;
	
	if cv2.waitKey(5) & 0xFF == ord('q'):
		break;


cap.release()
cv2.destroyAllWindows()

print(f'Global max min = {gMaxArea} - {gMinArea}')