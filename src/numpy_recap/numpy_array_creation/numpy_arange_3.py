import numpy as np
from numpy import ndarray

# 1D Array
arr_1D: ndarray = np.arange(6)
print(f'The Numpy array is:\n{arr_1D}')
print('********************************************')

# Convert the 1D array to 2D array: 2 rows , 3 columns
arr_2D_1: ndarray = arr_1D.reshape(2, 3)
print(f'The Numpy array is:\n{arr_2D_1}')
print('********************************************')

# Convert the 1D array to 2D array: 3 rows , 2 columns
arr_2D_2: ndarray = arr_1D.reshape(3, 2)
print(f'The Numpy array is:\n{arr_2D_2}')

