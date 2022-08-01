# First, let’s create a couple of DataFrames that will be using throughout this tutorial in order to demonstrate the
# various join types we will be discussing today.
import pandas as pd

df1 = pd.DataFrame(
    [
        (1, 345, 'B', True),
        (2, 100, 'C', False),
        (3, 300, 'B', False),
        (4, 151, 'A', False),
        (5, 212, 'A', True),
        (6, 121, 'C', False),
        (7, 333, 'B', True),
        (8, 456, 'C', True),
    ],
    columns=['id', 'value', 'colC', 'colD']
)
df2 = pd.DataFrame(
    [
        (1, 111, 10.1, 3),
        (9, 56, 3.33, 10),
        (10, 17, 18.0, 8),
        (3, 567, 19.1, 4),
        (11, 98, 2.1, 1),
        (6, 31, 3.14, 12),
    ],
    columns=['id', 'value', 'colE', 'colF']
)

print(f'Dataframe-1:\n{df1}')
print(f'Dataframe-1:\n{df2}')

# Inner Join
# df1.merge(df2, how='inner', on='id')
merged_dataframe = pd.merge(left=df1, right=df2, how='outer', on='id')

print(f'Merged Dataframe:\n{merged_dataframe}')
