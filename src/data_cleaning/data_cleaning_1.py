import pandas as pd

my_dict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
df = pd.DataFrame(my_dict)
print(f'Original Dataframe:\n{df}')

# Find out the rows where column 'a' =100
print(f'Dataframe where column "a" =100:\n{df[df.a == 100]}')

# get the rows where value of column 'a' is other than 100
df_new = df[df.a != 100]
print(f'Dataframe where column "a" !=100:\n{df_new}')

# Modify the column 'a' where the value is 100
df.loc[df['a'] == 100, 'a'] = 50
print(f'Modified Dataframe:\n{df}')

df["Texture"] = df["Texture"].replace(to_replace ="^l.*", value = 'loam', regex = True)
