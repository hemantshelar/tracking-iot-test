import cv2
import numpy as np
import matplotlib.pyplot as plot

def detect_face(img,face_cascade):
	face_img = img.copy();
	face_rects = face_cascade.detectMultiScale(face_img);
	print(face_rects)
	for ( x,y,w,h) in face_rects:
		cv2.rectangle(face_img,(x,y),(x+w,y+h),255,3)
	return face_img;

def showimg(img):
	result = None
	if len(img.shape) > 2:
		result = cv2.cvtColor(img,cv2.COLOR_BGR2RGB);
		plot.imshow(result);
	else:
		plot.imshow(img,cmap='gray')

aru = cv2.imread('denis1.jpg',0);
aru = cv2.imread('conf1.jpg',0);
#gray = cv2.cvtColor(aru,cv2.COLOR_BGR2GRAY)


#haarcascade_frontalface_default
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

#face_cascade.detectMultiScale(gray);

face_with_rect = detect_face(aru,face_cascade)


showimg(face_with_rect);
plot.show();

