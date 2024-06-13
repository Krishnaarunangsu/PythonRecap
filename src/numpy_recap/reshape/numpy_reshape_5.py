# Reshaping arrays
# Reshaping means changing the shape of an array.
# The shape of an array is the number of elements in each dimension.
# By reshaping we can add or remove dimensions or change number of elements in each dimension.

# Reshape From 1-D to 3-D
# Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

__author__ = "Arunangsu Sahu"
import numpy as np

arr=np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_arr=arr.reshape(4,2)
print(f' The New Re-shaped array is:\n{new_arr}')
print(f' Actual array is:\n{arr}')

new_arr=arr.reshape(2,4)
print(f' The New Re-shaped array is:\n{new_arr}')

new_arr=arr.reshape(2,2,2)
print(f' The New Re-shaped array is:\n{new_arr}')


