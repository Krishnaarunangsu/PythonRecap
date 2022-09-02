# Python program to demonstrate
# array creation techniques
import numpy as np

# Creating array from list with type float
a = np.array(
    [
        [1, 2, 4],
        [5, 8, 7]
    ],
    dtype='int')
print("Array created using passed list:\n", a)
