import pandas as pd

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])

# Conditional that returns a boolean Series
df_cond_1 = df.loc[df['shield'] > 6]
print(df_cond_1)

df_cond_2 = df.loc[df['shield'] < 6]
print(df_cond_2)

# Conditional that returns a boolean Series with column labels specified
df_cond_3 = df.loc[df['shield'] > 6, ['max_speed']]
print(df_cond_3)

# Callable that returns a boolean Series
df_cond_4 = df.loc[lambda df: df['shield'] == 8]
print(df_cond_4)
