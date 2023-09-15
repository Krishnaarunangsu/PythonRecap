import numpy as np

arr=[20, 2, 7, 1, 34]
print(f'The array is:{arr}')
print(f'The 25th Percentile of the array is:{np.percentile(arr,25)}')
print(f'The 50th Percentile of the array is:{np.percentile(arr,50)}')
print(f'The 75th Percentile of the array is:{np.percentile(arr,75)}')