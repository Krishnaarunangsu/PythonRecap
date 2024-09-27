import pandas as pd

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])

print(f'The original Dataframe is:\n{df}')
print('***************************')

# Single label. Note this returns the row as a Series.
print('Select Data for a Single Label: viper')
print(df.loc['viper'])
print('***************************')
# Single label for row and column
print(f'Shield Value of cobra:{df.loc["cobra", "shield"]}')
print('***************************')
# Slice with labels for row and single label for column. As mentioned above, note that both the start and stop of the
# slice are included.
print('Select Data for a range of row Labels: cobra, viper')
print(df.loc['cobra':'viper'])
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('Select a particular column(max_speed) for a range of row Labels: cobra, viper')
print(df.loc['cobra':'viper', 'max_speed'])
print('***************************')
# List of labels. Note using [[]] returns a DataFrame.
print('Select Data for a List of labels')
print(df.loc[['viper']])
print(df.loc[['viper', 'sidewinder']])
print('***************************')
# Slice with labels for row and list of labels for column. As mentioned above, note that both the start and stop of the
# slice are included.
print('max Speed for Cobra-Viper')
print(df.loc['cobra':'viper', 'max_speed'])
print(df.loc['cobra':'viper', ['max_speed']])# Column label will be shown
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print(df.loc['cobra':'viper', ['max_speed', 'shield']])
print(df.loc[['cobra', 'viper'], ['max_speed', 'shield']])
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print(df.loc['cobra':'sidewinder', ['max_speed', 'shield']])
print('***************************')
# Boolean list with the same length as the row axis
print(df.loc[[True, False, True]]) # details of cobra and sidewinder
print('***************************')
print('Boolean Mapping')
print(df.loc[pd.Series([False, True, False],
                       index=['viper', 'sidewinder', 'cobra'])])
