# Reshaping array: We can use reshape method to reshape an array. Consider an array with shape (a1, a2, a3, …,
# aN). We can reshape and convert it into another array with shape (b1, b2, b3, …, bM). The only required condition
# is: a1 x a2 x a3 … x aN = b1 x b2 x b3 … x bM . (i.e. original size of array remains unchanged.)
# numpy.reshape( array, shape, order = ‘C’) : Shapes an array without changing data of array.
import numpy as np

arr_1 = np.arange(8)
print(f'The Original Numpy array is::\n{arr_1}')

print(f'**********************************************')
# Reshaping the array with 2 rows and 4 columns(2, 4)
arr_2 = arr_1.reshape(2, 4)
print(f'The Re-shaped Numpy array is::\n{arr_2}')

print(f'**********************************************')
# Reshaping the array with 2 rows 2 columns along 2 axis (2,2,2)
arr_3 = arr_1.reshape(2, 2, 2)
print(f'The Re-shaped Numpy array is::\n{arr_3}')
