import numpy as np

list_1 = [1, 2, 3]
list_2 = [11, 21, 31]

num_3=np.array([
    list_1,list_2
])
print(num_3)
print(num_3.shape)
print(num_3.reshape(3,2))