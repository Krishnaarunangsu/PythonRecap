import pandas as pd

my_dict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
my_df = pd.DataFrame(my_dict)
print(f'The Dataframe is:\n{my_df}')
print('***************************************')
print(f'Row-1:\n{my_df.iloc[0]}')
print('***************************************')
print(f'Row-1:\n{my_df.iloc[[0]]}')
print('***************************************')
print(f'Row-1\n:{my_df.iloc[:1]}')
print('***************************************')
print(f'Row-1:\n{my_df[:1]}')
print('***************************************')
print(f'Row-1 and Row 2:\n{my_df.iloc[0:2]}')
print('***************************************')
print(f'Row-1 and Row 2:\n{my_df[0:2]}')
print('***************************************')
print(f'Row 1 and Row 3:\n{my_df.iloc[[True, False, True]]}')
print('***************************************')
print(f'Row 1 and Row 3:\n{my_df.iloc[lambda x: x.index%2==0]}')
print('***************************************')
# Row Column index
# 1st Row and 2nd column
print(f'Row 1 Column 2:\n{my_df.iloc[0,1]}')

# 1st and 2nd Rows and 1st and 3rd columns
print(f'Row 1 Column 2:\n{my_df.iloc[[0,1],[0,3]]}')

# With Slice Objects: 2nd and 3rd Row and 1st, 2nd and 3rd Columns
print(f'With Slice Objects:\n{my_df.iloc[1:3, 0:3]}')

# With a boolean array whose length matches the columns.
print(f'Range of columns with boolean values:\n{my_df.iloc[:,[True, False, True, False]]}')

# With a callable function that expects the Series or DataFrame.
print(f'With Callable function for the columns:\n{my_df.iloc[:, lambda df:[0,2]]}')

# With a callable function that expects the Series or DataFrame.
print(f'With Callable function for the rows:\n{my_df.iloc[lambda df:[0,2],:]}')