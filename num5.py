import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])
arr1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])


print('5th element on 2nd row: ', arr1[1, 4])
print('4th element on 1st row:',arr1[0,3])
arr3=np.array([[[1,2,39],[4,0,6]],[[7,8,9],[10,1,12]]])
print(arr3)
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr2[0, 1, 2])
