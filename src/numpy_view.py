import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
x = arr.view()
arr[0] = 42
print(arr)
print(x)
x[0] = 57
print(arr)
print(x)
