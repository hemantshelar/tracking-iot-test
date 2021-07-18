import numpy as np
import cv2

import matplotlib.pyplot as plot

img = cv2.imread('chessboard.jpg',0)
print(img);
print(img.shape)

arr = np.ravel(img);

print(arr.shape)
print(len(arr))
