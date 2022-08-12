import numpy as np

np_array_1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f'The numpy array is:\n{np_array_1}')
print('*****************************')
print(f'The first element of the numpy array:\n{np_array_1[0]}')
print('*****************************')
print(f'The first element of the numpy array with first 4 elements:\n{np_array_1[0][0:4]}')
print('*****************************')
# From the first element, slice elements from index 0 to index 4 (not included):
print(f'The first element of the numpy array with first 4 elements:\n{np_array_1[0, 0:4]}')
print('*****************************')
print(f'The second element of the numpy array:\n{np_array_1[1]}')
print('*****************************')
print(f'The second element of the numpy array with first 3 elements:\n{np_array_1[1][1:4]}')
print('*****************************')
# From the second element, slice elements from index 1 to index 4 (not included):
print(f'The second element of the numpy array with first 3 elements:\n{np_array_1[1, 1:4]}')
print('*****************************')
# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(f'Slice first 3 elements from both the array elements:\n{np_array_1[0:2, 1:4]}')
print('*****************************')
# print(np_array_1[0, 0:4, 1, 0:4])
arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[1:4])
