# import the libraries
import pandas as pd

# Scalar `to_replace` and `value`
from pandas import Series

# Replace a column-value in pandas series
series_1: Series = pd.Series([1, 2, 3, 4, 5])
print(f'Original Series:\n{series_1}')
series_1.replace(to_replace=1, value=5,
                 inplace=True)  # If In place is not used the original dataframe remains unchanged
print(f'Modified Series:\n{series_1}')

# replace a particular value in pandas dataframe
df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})
print(f'Original dataframe:\n{df}')
# replace 0 with 5 in the dataframe in all columns
df.replace(0, 5, inplace=True)
print(f'Modified dataframe:\n{df}')

# replace 5 with 7 in the dataframe in the column 'A
df['A'] = df['A'].replace(to_replace=5, value=7)
print(f'Modified dataframe:\n{df}')
