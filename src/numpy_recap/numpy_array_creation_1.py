# Import numpy library
import numpy as np

# In Python Array is actually a list
arr_1 = [1, 3, 4, 5, 6]
print(f'The type of the data structure is:\n{type(arr_1)}')
print('****************************************')
# Creating a Numpy Array from a list
arr_2 = np.array(arr_1)
print(f'The type of the data structure is:\n{type(arr_2)}')