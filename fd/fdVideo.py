import cv2
import numpy as np
import matplotlib.pyplot as plot

def detect_face(img,face_cascade):
	face_img = img.copy();
	face_img = cv2.cvtColor(face_img,cv2.COLOR_BGR2GRAY);
	face_rects = face_cascade.detectMultiScale(face_img);
	for ( x,y,w,h) in face_rects:
		cv2.rectangle(face_img,(x,y),(x+w,y+h),255,3)
	return face_img;

def adjusted_detect_face(img,face_cascade):
	face_img = img.copy();
	face_img = cv2.cvtColor(face_img,cv2.COLOR_BGR2GRAY);
	face_rects = face_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=5);
	for ( x,y,w,h) in face_rects:
		cv2.rectangle(face_img,(x,y),(x+w,y+h),255,3)
	return face_img;

cap = cv2.VideoCapture(0);

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

while True:
	ret,frame = cap.read();
	f = adjusted_detect_face(frame,face_cascade);
	cv2.imshow("Live",f);
	if cv2.waitKey(5) & 0xFF == ord('q'):
		break;
cap.release();
cv2.destroyAllWindows();
