# My Name : George Hany

# print the following Attributes :–
# 1) The shape of an array.
# 2) Array dimensions.
# 3) The Length of each element of the array in bytes.

# importing the numpy library
import numpy as np

# Note: The element must be a type of unsigned int16.
arr = np.empty((2, 4), dtype = np.uint16)
print(arr)
print()

print('Printing NumPy array Attributes')
print()
print('1) Array Shape is : ', arr.shape)
print()
print('2) Array dimensions are : ', arr.ndim)
print()
print('3) Length of each element of array in bytes is : ', arr.itemsize)