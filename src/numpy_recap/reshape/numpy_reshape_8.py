# Unknown Dimension
# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.

__author__ = "Arunangsu Sahu"
import numpy as np

arr=np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_arr=arr.reshape(2,2, -1)
print(f'The new Array is:\n{new_arr}')



