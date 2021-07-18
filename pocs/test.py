import numpy as py
import cv2
import math
import matplotlib.pyplot as plot

import ..\utils\plotimages

imageList = []


aru = cv2.imread('../imgs/aru.jpg')
cat = cv2.imread('../imgs/cat.jpg')
aa = cv2.imread('../imgs/aa.jpg')
h = cv2.imread('../imgs/h.jpg')

imageList.append(aru);
imageList.append(cat);
imageList.append(aa);
imageList.append(h);


print(imageList[0])
print(len(imageList))

showImages(imageList,3)





