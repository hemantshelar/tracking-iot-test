import numpy as py
import cv2
import math
import matplotlib.pyplot as plot

imageList = []

def addImage(image):
	imageList.append(image)

def showImages(columns):
	index = 1;
	count = len(imageList)
	rows = count / columns;
	rows = math.ceil(rows)

	for i in range(rows):
		for j in range(columns):
			if index > len(imageList):
				break;
			subPlotArgs = f'{rows}{columns}{index}'
			plot.subplot(subPlotArgs)
			img = cv2.cvtColor(imageList[index-1],cv2.COLOR_BGR2RGB)
			plot.imshow(img)
			index = index + 1
	
	plot.show();