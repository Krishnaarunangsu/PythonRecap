# One of the efficient and pandaic way is using eq()  and ne() method:

import pandas as pd

my_dict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
df = pd.DataFrame(my_dict)
print(f'Original Dataframe:\n{df}')

# Find out the rows where column 'a' =100
df_bool = df['a'] == 100
print('*********************')
print(f'Boolean:\n{df_bool}')

df_dup = df[df['a'] == 100]
print('*********************')
print(f'Duplicate Records:\n{df_dup}')

# get the rows where value of column 'a' is other than 100
df_bool = df['a'] != 100
print('*********************')
print(f'Boolean:\n{df_bool}')

df_non_dup = df[df['a'] != 100]
print('*********************')
print(f'Non-Duplicate Records:\n{df_non_dup}')

df_new = df.drop(df_non_dup.index)
print(f'Non-Duplicate Records:\n{df_new}')
