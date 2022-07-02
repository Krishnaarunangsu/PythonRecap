import numpy as np

array_1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# From the first element, slice elements from index 0 to index 4 (not included):
print(array_1[0, 0:4])
print('*****************************')
# From the second element, slice elements from index 1 to index 4 (not included):
print(array_1[1, 1:4])

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(array_1[0:2, 1:4])

# print(array_1[0, 0:4, 1, 1:3])

arr = np.array([10, 15, 20, 25, 30, 35, 40])

print(arr[1:4])
