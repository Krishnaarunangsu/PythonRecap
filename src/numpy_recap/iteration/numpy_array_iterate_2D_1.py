# Iterate on the elements of the following 2-D array:

import numpy as np

arr_2D = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)
print(f'The 2D array is:\n{arr_2D}')
print('********************************************************')

for x in arr_2D:
    print(f'Array element is:{x}')
print('********************************************************')

for index, value in enumerate(arr_2D):
    print(f'Array element at {index} position is {value}')
for value in arr_2D:
    print('********************************************************')
    print(f'Array element is:{value}')
    print('********************************************************')
    for index,value_scalar in enumerate(value):
        print(f'Scalar Array element at {index} position is {value_scalar}')




