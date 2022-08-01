import pandas as pd

# List
a = [1, 7, 2]

# Create a Series
my_series = pd.Series(a)
print(f'My Series:\n{my_series}')
print(f'Type of Data Structure:{type(my_series)}')

# My Series with Label
my_labelled_series = pd.Series(a, index=['x', 'y', 'z'])
print(f'My Series:\n{my_labelled_series}')

data = {
    'apples': [3, 2, 0, 1]
}

series_1 = pd.Series(data)
print(f'My Series:\n{series_1}')
