import numpy as np

# NumPy offers several functions to create arrays with initial placeholder content.
# These minimize the necessity of growing arrays, an expensive operation.
# For example: np.zeros,np.empty etc.

# numpy.zeros(shape, dtype = float, order = ‘C’) :
# Return a new array of given shape and type, with random values. order:(C,F): row-major, column-major

# Python Programming illustrating numpy.empty method
arr_1 = np.zeros(2, dtype=int)
print(f'The Initialized array is: {arr_1}')
print(f'The Shape of the array is :{arr_1.shape}')

print('***********************************************************')
arr_2 = np.zeros([2, 2], dtype=int)
print(f'The Initialized array is: {arr_2}')
print(f'The Shape of the array is :{arr_2.shape}')

print('***********************************************************')
arr_3 = np.zeros([3, 3])
print(f'The Initialized array is: {arr_3}')
print(f'The Shape of the array is :{arr_3.shape}')
