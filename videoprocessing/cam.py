import cv2;
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0);
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

writer = cv2.VideoWriter('test.mp4',cv2.VideoWriter_fourcc(*'DIVX'),20,(w,h))
print ( f'w={w} h={h} fps={fps}');

while True:
	ret,frame = cap.read();
	cv2.imshow('w',frame)
	writer.write(frame);

	if cv2.waitKey(5) & 0xFF == ord('q'):
		break;
cap.release();
writer.release();
cv2.destroyAllWindows();

	