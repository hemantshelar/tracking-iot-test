import cv2;
import numpy as np



#a1 = np.arange(0,99,1,dtype=np.uint8)

#a11 = a1.reshape(-1,1)

#print(a1)

#print ( a11.shape )

#print ( a11 )

points = np.array([[0,0] ,[200,100], [200,250]],np.int32)
print ( points.shape)

bi = np.zeros((512,512,3),np.uint8)
print ( bi.shape);

cv2.imshow('Black',bi);

points = points.reshape((-1,1,2))

cv2.polylines(bi,[points],True,(255,0,255),6)

cv2.imshow('Black',bi);

cv2.waitKey();
