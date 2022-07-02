import pandas as pd

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])

print(df)
print('***************************')

# Single label. Note this returns the row as a Series.
print('Single Label')
print(df.loc['viper'])
print('***************************')
# List of labels. Note using [[]] returns a DataFrame.
print('List of labels')
print(df.loc[['viper']])
print(df.loc[['viper', 'sidewinder']])
print('***************************')
# Single label for row and column
print('Single label for row and column')
print(df.loc['cobra', 'shield'])
print('***************************')
# Slice with labels for row and single label for column. As mentioned above, note that both the start and stop of the
# slice are included.
print(df.loc['cobra':'viper', 'max_speed'])
print('***************************')
# Slice with labels for row and list of labels for column. As mentioned above, note that both the start and stop of the
# slice are included.
print(df.loc['cobra':'viper', ['max_speed']])
print(df.loc['cobra':'viper', ['max_speed', 'shield']])
print(df.loc[['cobra', 'viper'], ['max_speed', 'shield']])
print(df.loc['cobra':'sidewinder', ['max_speed', 'shield']])
print('***************************')
# Boolean list with the same length as the row axis
print(df.loc[[True, False, True]])
print('***************************')
print('Boolean Mapping')
print(df.loc[pd.Series([False, True, False],
                       index=['viper', 'sidewinder', 'cobra'])])
