import pandas as pd

df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})
print(f'Original Dataframe:\n{df}')

# Dict-like `to_replace`
df_1 = df.replace(to_replace={0: 10, 1: 100})
print(f'Modified Dataframe:\n{df_1}')  # assigned the change in a nw Dataframe so no "inplace" in the existing dataframe


df_3 = df.replace(to_replace={'A': {0: 100, 4: 400}})
print(f'Modified Dataframe:\n{df_3}')  # assigned the change in a nw Dataframe so no "inplace" in the existing dataframe
