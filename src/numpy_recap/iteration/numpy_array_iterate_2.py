import numpy as np

# creating an array using arrange method
a = np.arange(12)

# shape array with 3 rows and 4 columns
a = a.reshape(3, 4)
print(f'Original array is:\n{a}')
print('****************************************************')

print('Array Iteration:')

# iterating  an array
for x in np.nditer(a):
    print(x)
print('****************************************************')

# Transposing the Original array
b = a.T
print('Iteration of the Transposed Array:')
# iterating the transposed array
for x in np.nditer(b):
    print(x)
