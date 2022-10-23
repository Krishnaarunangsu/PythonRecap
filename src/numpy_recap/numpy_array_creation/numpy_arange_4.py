import numpy as np
from numpy import ndarray

# 1D Array
arr_1D: ndarray = np.arange(12)
print(f'The Numpy array is:\n{arr_1D}')
print('*********************************************')

# Convert the 1D array to 3D array
arr_3D_1: ndarray = arr_1D.reshape(2, 3, 2)
print(f'The Numpy array is:\n{arr_3D_1}')
print('*********************************************')


# Convert the 1D array to 3D array
arr_3D_1: ndarray = arr_1D.reshape(2, 2, 3)
print(f'The Numpy array is:\n{arr_3D_1}')
print('*********************************************')


# Convert the 1D array to 3D array
arr_3D_2: ndarray = arr_1D.reshape(3, 2, 2)
print(f'The Numpy array is:\n{arr_3D_2}')



