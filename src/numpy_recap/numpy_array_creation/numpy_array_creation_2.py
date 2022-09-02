# Python code to demonstrate the working of array()
# Import numpy library
import numpy as np
# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr_1 = array.array('i', [1, 2, 3])
print(arr_1)
print(type(arr_1))
# printing original array
print("The new created array is : ", end="")

for i in arr_1:
    print(f'The array element is:{i}')

print('***************************')
try:
    for i in range(0, len(arr_1)):
        print(f'arr_1[{i}]={arr_1[i]}', end=", ")
except IndexError as ie:
    print(ie)

print("\r")

arr_2 = np.array(arr_1)
print(f'The Created Numpy array from the array is:\n{arr_2}')

int_array = array.array('i', [1, 2, 3, 4])

for a in int_array:
    print(a)
