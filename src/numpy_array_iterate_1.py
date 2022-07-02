import numpy as np

numpy_arr_1 = np.array([5, 7, 6])

for a in numpy_arr_1:
    print(f"{a}")

# my_list = [21, 44, 35, 11]

for index, val in enumerate(numpy_arr_1):
    print(f'The element in the {index} is {val}')
