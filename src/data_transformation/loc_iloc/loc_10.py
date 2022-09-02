import pandas as pd

tuples = [
    ('cobra', 'mark i'), ('cobra', 'mark ii'),
    ('sidewinder', 'mark i'), ('sidewinder', 'mark ii'),
    ('viper', 'mark ii'), ('viper', 'mark iii')
]
print(tuples)

index = pd.MultiIndex.from_tuples(tuples)

values = [[12, 2], [0, 4], [10, 20],
          [1, 4], [7, 1], [16, 36]]

# Build the dataframe
df = pd.DataFrame(values, columns=['max_speed', 'shield'], index=index)
print(df)

# Single label. Note this returns a DataFrame with a single index.
print(df.loc['cobra'])

# Single index tuple. Note this returns a Series.
print(df.loc[('cobra', 'mark ii')])

# Single label for row and column. Similar to passing in a tuple, this returns a Series.
print(df.loc['cobra', 'mark ii'])

# Single tuple. Note using [[]] returns a DataFrame.
print(df.loc[[('cobra', 'mark ii')]])

# Single tuple for the index with a single label for the column
print(df.loc[('cobra', 'mark i'), 'shield'])

# Slice from index tuple to single label
print(df.loc[('cobra', 'mark i'):'sidewinder'])

# Slice from index tuple to index tuple
print(df.loc[('cobra', 'mark i'):('viper', 'mark ii')])
