# numpy basics
import numpy as np

numpy_array_1 = np.arange(15).reshape(3, 5)
print(f"Numpy array is:{numpy_array_1}")
print(f"The shape of the array is:{numpy_array_1.shape}")
print(f"The dimension of the array is:{numpy_array_1.ndim}")
print(f"The data type of the array is:{numpy_array_1.dtype}")
print(f"The name of the data type of the array is:{numpy_array_1.dtype.name}")
print(f"The item size of the array is:{numpy_array_1.itemsize}")
print(f"The type of the array is:{type(numpy_array_1)}")
