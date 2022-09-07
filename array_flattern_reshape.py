from numpy import *
arr1 = array([[1,2,4,5,6],[5,3,21,34,4]])
print(arr1)
print(arr1.ndim)
print(arr1.size)
arr2 = arr1.flatten()
print(arr2)
arr3 = arr1.reshape(5,2)
print(arr3)
