import numpy as np

array_1 = np.array([0, 1, 2])
array_2 = array_1 + 5

print(f'Sum after Heterogeneous Broadcasting:{array_2}')
print('******************************************************')

array_3 = np.ones((3, 3))

print(f'The Ones array is:\n{array_3}')
array_4 = array_3+array_1
print(f'Sum after Heterogeneous Broadcasting:\n{array_4}')
