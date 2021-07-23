import numpy as np
import cv2


#List is array of pointers
#NumPy is continuous block of array

a = np.array([1,2,3,4])
x = np.where(a == 4);
print ( x)


b = np.array([1,0,1,0])
a[b==0] = 100;
print(a);
print(b);

a = np.arange(1,12,2)
print(a)

a = np.linspace(1,12,6)
print(a)


a = a.reshape(3,2)
print(a)

print(a[2][1])


########################################
a = np.zeros((10,10,3),dtype=np.int8)
a[9][9][0] = 10
a[0][0][0] = 11;
print(a);

result = np.where(a == 11);
print(result)

print(a.size)
print(a.shape)
print(a.dtype)