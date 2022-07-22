import pandas as pd

df = pd.DataFrame({'A': ['bat', 'foo', 'bait'],
                   'B': ['abc', 'bar', 'xyz']})

print(f'Original Dataframe:\n{df}')

# Across the dataframe
df_1 = df.replace(to_replace=r'^ba.$', value='new', regex=True)
print(f'Modified Dataframe:\n{df_1}')

# In one column
df_2 = df.replace({'A': r'^ba.$'}, {'A': 'new'}, regex=True)
print(f'Modified Dataframe:\n{df_2}')

df_3 = df.replace(regex=r'^ba.$', value='new')
print(f'Modified Dataframe:\n{df_3}')

df_4 = df.replace(regex={r'^ba.$': 'new', 'foo': 'xyz'})
print(f'Modified Dataframe:\n{df_4}')

df_5 = df.replace(regex=[r'^ba.$', 'foo'], value='new')
print(f'Modified Dataframe:\n{df_5}')

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html
