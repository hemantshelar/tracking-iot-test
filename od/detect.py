#water shaded
#Haar Cascades to detect

import cv2
import numpy as np
import matplotlib.pyplot as plot


#template matching

full = cv2.imread('aa.jpg')

subset = full[2000:3000,500:1500]

methods = ['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR','cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']

#for m in methods:
#	#create copy of image
#	full_coyp = full.copy();
#	method = eval(m);

#	res = cv2.matchTemplate(full_coyp,subset,method)
	#min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res);

#	print(res)

res = cv2.matchTemplate(c,subset,cv2.TM_CCOEFF)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

print(f'{min_val} {max_val} {min_loc} {max_loc}')
topLeft = max_loc;

height,width,channels = subset.shape
print(f'{height} {width} {channels}')
bottomRight = (max_loc[0]+width,max_loc[1]+height)

cv2.rectangle(c,topLeft,bottomRight,(255,0,0),10)




plot.subplot(131)
plot.imshow(res)
plot.subplot(132)
plot.imshow(c)
plot.subplot(133)
plot.imshow(c)
plot.show();
	

#plot.imshow(clip)
#plot.show();


