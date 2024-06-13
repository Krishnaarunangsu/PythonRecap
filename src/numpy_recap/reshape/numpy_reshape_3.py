# Reshaping arrays
# Reshaping means changing the shape of an array.
# The shape of an array is the number of elements in each dimension.
# By reshaping we can add or remove dimensions or change number of elements in each dimension.

# Reshape From 1-D to 2-D
# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:

__author__ = "Arunangsu Sahu"
import numpy as np

arr=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr=arr.reshape(4, 3)
print(f' The New Re-shaped array is:\n{new_arr}')


