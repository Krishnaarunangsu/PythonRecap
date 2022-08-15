# Iterate numpy array elements

import numpy as np

np_array = np.array([[1, 2], [3, 4]])
print(np_array)
for val in np.nditer(np_array):
    print(val)
