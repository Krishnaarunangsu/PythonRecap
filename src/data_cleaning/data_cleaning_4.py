# One of the efficient and pandaic way is using eq()  and ne() method:

import pandas as pd

my_dict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
df = pd.DataFrame(my_dict)
print(f'Original Dataframe:\n{df}')

# Find out the rows where column 'a' =100
df_dup = df.query("a==100")
print(df_dup)

# get the rows where value of column 'a' is other than 100
df_non_dup = df.query("a!=100")
print(df_non_dup)
