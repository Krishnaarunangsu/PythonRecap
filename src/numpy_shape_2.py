import numpy as np

# Number of dimensions =  Number of Square brackets
arr = np.array([1, 2, 3, 4])
print(f'The array is :{arr}')
print('shape of array :', arr.shape)
print('******************')
# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has
# value 4:
arr = np.array([1, 2, 3, 4], ndmin=5)
print(f'The array is :{arr}')
print('shape of array :', arr.shape)
