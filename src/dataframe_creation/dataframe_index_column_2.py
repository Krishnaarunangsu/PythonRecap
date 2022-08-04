# Python code demonstrate to create a Pandas DataFrame with lists of dictionaries as well as row and column indexes.

import pandas as pd

# Initialize lists data. It is a list of dictionaries
data = [
    {
        'a': 1,
        'b': 2
    },
    {
        'a': 5,
        'b': 10,
        'c': 20
    }
]
index = ['first', 'second']
columns_1 = ['a', 'b']

# With two column indices, values same
# as dictionary keys
df1 = pd.DataFrame(data, index=index, columns=columns_1)

columns_2 = ['a', 'b1']
# With two column indices with
# one index with other name
df2 = pd.DataFrame(data, index=index, columns=columns_2)

# print for first data frame
print(df1, "\n")

# Print for second DataFrame.
print(df2)
