import pandas as pd

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])

# Set value for all items matching the list of labels
df.loc[['viper', 'sidewinder'], ['shield']] = 50
print(df)

# Set value for an entire row
df.loc['cobra'] = 10
print(df)
# Set value for an entire row with list label
df.loc[['cobra']] = 10
print(df)

# Set value for an entire column
df.loc[:, 'max_speed'] = 30
print(df)

# Set value for rows matching callable condition
df.loc[df['shield'] > 35] = 0
print(df)
