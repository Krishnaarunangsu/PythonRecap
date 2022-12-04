# Calculations with missing data
# Missing values propagate naturally through arithmetic operations between pandas objects.

import numpy as np
import pandas as pd

df_a = pd.DataFrame(
    np.random.randn(5, 2),
    index=["a", "c", "e", "f", "h"],
    columns=["one", "two"],
)
print(f'The Original df_a is:\n{df_a}')
print('*********************************************')

df_b = pd.DataFrame(
    np.random.randn(5, 3),
    index=["a", "c", "e", "f", "h"],
    columns=["one", "two", "three"],
)
print(f'The Original df_b is:\n{df_b}')
print('*********************************************')
print(df_a.loc['a':'c', 'one'])
print('*********************************************')
# df.loc['a', 'one'] = np.nan
# print(f'The Modified Dataframe is:\n{df}')

# Transforming dataframe df_a
df_a.loc['a':'c', 'one'] = np.nan
print(f'The Modified Dataframe df_a is:\n{df_a}')
print('*********************************************')
# Transforming dataframe df_b
df_b.loc[['a','c','h'], 'one'] = np.nan
print(f'The Modified Dataframe df_b is:\n{df_b}')

# Adding two dataframes(arithmetic operation))
df_c = df_a+df_b
print(f'The resultant dataframe df_c is:\n{df_c}')
