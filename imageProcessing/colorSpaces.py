import cv2
import numpy as np
#Color Spaces

#HSL - Hue Saturation Lightness
#White is at the top of Cylinder 

#HSV - Hue Saturation Value
# White is center of cylinder

#cvtColor
#Blending images togetaher 

def resizeImages(img,x,y):
	resized = cv2.resize(img,(0,0),None,x,y)
	return resized


aru = cv2.imread('../imgs/h.jpg')
hemant = cv2.imread('../imgs/a.jpg')
x = 1/3;
y = 1/3;
aru = resizeImages(aru,x,y)
hemant = resizeImages(hemant,x,y)

print( f'{aru.size} - {hemant.size}');

result = cv2.addWeighted(hemant,0.5,aru,0.5,0.1)
cv2.imshow('Aru',aru)
cv2.imshow('Hemant',hemant)
cv2.imshow('Result',result)

cv2.waitKey();
cv2.destroyAllWindows();