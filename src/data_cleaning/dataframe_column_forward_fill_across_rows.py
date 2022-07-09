# Example #1: Use ffill() function to fill the missing values along the index axis. Note : When ffill() is applied
# across the index then any missing value is filled based on the corresponding value in the previous row.

import pandas as pd

# # Creating the dataframe
df = pd.DataFrame({"A": [5, 3, None, 4],
                   "B": [None, 2, 4, 3],
                   "C": [4, 3, 8, 5],
                   "D": [5, 4, 2, None]})

print(f'Original Dataframe:\n{df}')

# Let’s fill the missing value over the index axis
# applying ffill() method to fill the missing values
df_2 = df.ffill(axis=0)
print(f'Modified Dataframe:\n{df_2}')

# Example #2: Use ffill() function to fill the missing values along the column axis.
# Note : When ffill is applied across the column axis,
# then missing values are filled by the value in previous column in the same row.
df_3 = df.ffill(axis=1)
print(f'Modified Dataframe:\n{df_3}')

