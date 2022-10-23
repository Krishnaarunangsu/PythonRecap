# Python program to demonstrate basic array characteristics
import numpy as np

# Creating array object
arr = np.array(
    [
        [1, 2, 3],
        [4, 2, 5]
    ]
)

# Printing type of arr object
print("Array is of type: ", type(arr))
print('***********************************************')

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)
print('***********************************************')

# Printing shape of array
print("Shape of array: ", arr.shape)
print('***********************************************')

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)
print('***********************************************')

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)
