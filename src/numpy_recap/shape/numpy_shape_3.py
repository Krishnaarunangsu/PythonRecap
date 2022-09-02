import numpy as np

array_1 = np.array([[2, 3], [4, 5]])
print(f'Shape of the array:\n{array_1.shape}')
print(array_1.shape[0])

arr2 = np.array([[4, 2, 3, 2, 1, 8],
                 [5, 4, 6, 7, 8, 9]])
res = np.shape(arr2)

print(res)

arr3 = arr2.reshape(2, 3, 2)

print(arr3)

arr_4 = np.array([[2, 3], [3, 4], [4, 5]])
b = np.shape(arr_4)
print('Column shape=', arr_4.shape[1])
print('Array Shape = ', np.shape(arr_4))

arr_5 = np.array([[2, 3, 1], [3, 4, 2], [4, 5, 3]])
b = np.shape(arr_5)
print('Column shape=', arr_5.shape[1])
print('Array Shape = ', np.shape(arr_5))
