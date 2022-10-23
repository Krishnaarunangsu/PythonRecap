# Create 2D numpy array
import numpy as np

data_1 = [
           [1, 2],
           [3, 4]
        ]
numpy_array_2D = np.array(object=data_1)

print(f'The NumPy Array is:\n{numpy_array_2D}')
print('**********')
print(f'The Dimension of the NumPy Array is:{numpy_array_2D.ndim}')
