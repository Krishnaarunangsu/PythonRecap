import numpy as np
import pandas as pd

sample_array = np.array([[1, 2, 3], [4, 5, 6]])
print(sample_array)
print(sample_array[1, 1])

series_1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(series_1['a'])

series_2 = pd.Series(np.random.randn(2))
print(series_2.size)
