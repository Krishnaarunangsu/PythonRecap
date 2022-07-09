import pandas as pd

# Create a dataframe
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
print(f'Original Data:\n{df}')

# Insert a new column 'newcol' at the colum index 1
df.insert(loc=1, column='newcol', value=[99, 99])
print(f'Modified Data:\n{df}')

# Allow Duplicate Column
df.insert(loc=0, column='col1', value=[100, 100], allow_duplicates=True)
print(f'Modified Data:\n{df}')

# Notice that pandas uses index alignment in case of value from type Series:
df.insert(loc=0, column="col0", value=pd.Series([5, 6], index=[0, 1]))
# df.insert(loc=0, column="col0", value=pd.Series([5, 6], index=[0, 1]))
# df.insert(loc=0, column="col0", value=pd.Series([5, 6], index=[0, 2]))
print(f'Modified Data:\n{df}')
