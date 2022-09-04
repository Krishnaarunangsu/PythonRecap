# Create 3D numpy array
import numpy as np


data_1 = [
           [
             [1, 2],
             [3, 4],
             [5, 6],
             [7, 8]
        ]
    ]

numpy_array_3D = np.array(object=data_1)

print(f'The NumPy Array is:\n{numpy_array_3D}')
print('*****************************************')
print(f'The Dimension of the NumPy Array is:{numpy_array_3D.ndim}')