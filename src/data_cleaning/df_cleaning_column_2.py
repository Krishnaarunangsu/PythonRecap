import pandas as pd

df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})
print(f'Original Dataframe:\n{df}')

# List-like `to_replace`
df_1 = df.replace(to_replace=[0, 1, 2, 3], value=4)
print(f'Modified Dataframe:\n{df_1}')  # assigned the change in a nw Dataframe so no "inplace" in the existing dataframe

df_2 = df.replace(to_replace=[0, 1, 2, 3], value=[4, 3, 2, 1])
print(f'Modified Dataframe:\n{df_2}')  # assigned the change in a nw Dataframe so no "inplace" in the existing dataframe
