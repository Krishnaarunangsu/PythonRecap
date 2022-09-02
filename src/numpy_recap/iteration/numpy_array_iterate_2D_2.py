# Iterate numpy array elements

import numpy as np

np_array = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)
print(f'The 2D NumPy Array is:\n{np_array}')
print('*************************************************')

for val in np.nditer(np_array):
    print(f'The array element in the 1st level is:{val}')
