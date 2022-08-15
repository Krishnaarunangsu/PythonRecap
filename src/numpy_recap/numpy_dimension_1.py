# Forming a nupy array from two other numpy arrays


import numpy as np

np_array1 = np.array([1, 2, 3])
np_array2 = np.array([4, 5, 6])
np_array = np.array([np_array1, np_array2])
print(f'The numpy array is:\n{np_array}')
print(f'The dimensions of the numpy array is:{np_array.ndim}')

for val in np_array:
    print(val)
