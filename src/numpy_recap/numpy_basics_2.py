# numpy basics
import numpy as np

# Zeros: 3 rows x 4 columns
print(f'Numpy Zeros:\n{np.zeros((3,4))}')

# Ones: 2 Sets: 3 rows x 4 columns
print(f'Numpy Ones:\n{np.ones((2,3,4), dtype=np.int16)}')

# Creating an array of evenly spaced values
print(f'Array of evenly spaced value:\n{np.arange(10, 25, 5)}')

# Evenly spaced samples
print(f'Evenly spaced samples:\n{np.linspace(0,2,9)}')

# Identity Matrix
print(f'Identity Matrix:\n{np.full((2,2), 9)}')
print(f'Identity Matrix:\n{np.eye(2)}')
print(f'Identity Matrix:\n{np.eye(3)}')
print(f'Identity Matrix:\n{np.eye(4)}')

# Create an array with random values
print(f'Random Values:\n{np.random.random((2, 2))}')

# Create an empty array
print(f'The Empty array is :\n{np.empty((3,2))}')


