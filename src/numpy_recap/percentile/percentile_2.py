import numpy as np

arr=[[14,17,12,33,44],
     [15,6,27,8,19],
     [23, 2,54, 1, 4]]
print(f'The array is:\n{arr}')
print('**********************************************************')
# Percentile of the flattened array
print(f'The 0th Percentile of the array is:{np.percentile(arr,0)}')
print('###############################################################')
print(f'The 25th Percentile of the array is:{np.percentile(arr,25)}')
print('###############################################################')
print(f'The 50th Percentile of the array is:{np.percentile(arr,50)}')
print('###############################################################')
print(f'The 75th Percentile of the array is:{np.percentile(arr,75)}')
print('**********************************************************')

# Percentile along the axis = 0
print('******************Percentile along the axis = 0*********************')
print(f'The 0th Percentile of the array is:{np.percentile(arr,0,axis=0)}')
print('###############################################################')
print(f'The 25th Percentile of the array is:{np.percentile(arr,25,axis=0)}')
print('###############################################################')
print(f'The 50th Percentile of the array is:{np.percentile(arr,50,axis=0)}')
print('###############################################################')
print(f'The 75th Percentile of the array is:{np.percentile(arr,75,axis=0)}')
print('**********************************************************')

# Percentile along the axis = 1
print('******************Percentile along the axis = 1*********************')
print(f'The 0th Percentile of the array is:{np.percentile(arr,0,axis=1)}')
print('###############################################################')
print(f'The 25th Percentile of the array is:{np.percentile(arr,25,axis=1)}')
print('###############################################################')
print(f'The 50th Percentile of the array is:{np.percentile(arr,50,axis=1)}')
print('###############################################################')
print(f'The 75th Percentile of the array is:{np.percentile(arr,75,axis=1)}')
print('**********************************************************')

# Percentile along the axis = 1, keepdims=True
print('******************Percentile along the axis = 1,keepdims=True *********************')
print(f'The 0th Percentile of the array is:\n{np.percentile(arr,0,axis=1, keepdims=True)}')
print('###############################################################')
print(f'The 25th Percentile of the array is:\n{np.percentile(arr,25,axis=1, keepdims=True)}')
print('###############################################################')
print(f'The 50th Percentile of the array is:\n{np.percentile(arr,50,axis=1, keepdims=True)}')
print('###############################################################')
print(f'The 75th Percentile of the array is:\n{np.percentile(arr,75,axis=1, keepdims=True)}')