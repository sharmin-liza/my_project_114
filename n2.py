import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr)
print(arr.dtype)
arr = np.array([1, 2, 3, 4])

print(arr.dtype)
arr1 = np.array(['apple', 'banana', 'cherry'])

print(arr1.dtype)
arr1=np.array(['aplle','balle','calle'])
print(arr1)
arr2=np.array([2,3,5,6,9],dtype='S')
print(arr2)
print(arr2.dtype)
arr2 = np.array([1, 2, 3, 4], dtype='S')

print(arr2)
print(arr2.dtype)
arr3 = np.array([1, 2, 3, 4], dtype='i4')

print(arr3)
print(arr3.dtype)
arr3=np.array([1,2,3,5,6,0],dtype='i4')
print(arr3)
print(arr3.dtype)
arr4=np.array([1.1,2.2,3.3,4.4])
newarr=arr.astype(int)

arr4 = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

print(newarr)
print(newarr.dtype)
arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)