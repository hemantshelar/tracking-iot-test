import numpy as np
import cv2
import matplotlib.pyplot as plt


def resizeImages(img,x,y):
	resized = cv2.resize(img,(0,0),None,x,y)
	return resized
def showImage(mat,img):
	cv2.imshow(mat,img);
def showImagePlt(img):
	ti = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	plt.imshow(ti)


img = cv2.imread('../imgs/aa.jpg')
img = resizeImages(img,1/5,1/5)


sobelX = cv2.Sobel(img,cv2.CV_64F,1,0,2)
sobelY = cv2.Sobel(img,cv2.CV_64F,0,1,2)
laplacian = cv2.Laplacian(img,cv2.CV_64F)



cat = cv2.imread('../imgs/cat.jpg')
showImage('cat',cat);
showImagePlt(img);
showImagePlt(cat);

histb = cv2.calcHist([cat],[0],mask=None,histSize=[256],ranges=[0,256])
print(histb.shape)
plt.plot(histb)
plt.show()



#showImage('cat',cat)


cv2.waitKey();
cv2.destroyAllWindows();


#addWeighted
#Histogram
#Frequencies of values of color
#Histogram equalization 32 - needs hands on HSV to 


