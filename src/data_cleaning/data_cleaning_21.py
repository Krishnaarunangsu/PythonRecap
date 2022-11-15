import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(5, 3),
    index=['a', 'c', 'e', 'f', 'h'],
    columns=['one', 'two', 'three']
)

print(f'The Original Dataframe is:\n{df}')
print('*************************************************')

df["four"] = "bar"
print(f'The Modified Dataframe is:\n{df}')
print('*************************************************')

df["five"] = df["one"] > 0  # boolean check an storing results in a new column
print(f'The Modified Dataframe is:\n{df}')
print('*************************************************')

# Re-indexing the original dataframe
df_2 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g','h'])
print(f'The New Dataframe is:\n{df_2}')
print('*************************************************')
# Checking isna() on the new dataframe
print(f'Is-NA check:\n{pd.isna(df_2)}')
print('*************************************************')

# Checking notna() on the new dataframe
print(f'Not-NA check:\n{pd.notna(df_2)}')
print('*************************************************')

# Checking notnull() on the new dataframe
print(f'Not-NULL check:\n{pd.notnull(df_2)}')
print('*************************************************')

# Checking isna on column "one"
print(f'Is-NA check on Column "one":\n{pd.isna(df_2["one"])}')
print('*************************************************')

# Checking notna() on the new dataframe
print(f'Not-NA check on Column "four":\n{pd.notna(df_2["four"])}')
print('*************************************************')

# One has to be mindful that in Python (and NumPy), the nan's don’t compare equal,
# but None's do. Note that pandas/NumPy uses the fact that np.nan != np.nan,
# and treats None like np.nan.

# Comparing None with None
print(f'Comparing None with None:{None == None}')
print('*************************************************')
# Comparing numpy/pandas nan with nan
print(f'Comparing nan with nan:{np.nan == np.nan}')
print('*************************************************')

# Comparing a column with nan
print(f'Comparing a column with nan:\n{df_2["one"] == np.nan}')
print('*************************************************')

df_2["timestamp"] = pd.Timestamp("20220101")
print(f'The Modified New Dataframe is:\n{df_2["timestamp"]}')
print('*************************************************')

# Making some rows and columns nan
# rows = a, c, h
# columns = one, timestamp
df_2.loc[["a", "c", "h"], ["one", "timestamp"]] = np.nan
print(f'The modified dataframe is:\n{df_2}')

# Types of dTypes count
print(f'dTypes value counts:\n{df_2.dtypes.value_counts()}')
