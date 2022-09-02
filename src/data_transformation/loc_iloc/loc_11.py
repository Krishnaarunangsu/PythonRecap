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

tuples_1 = [('bar', 'one'), ('bar', 'two'),
            ('baz', 'one'), ('baz', 'two')]

index_1 = pd.MultiIndex.from_tuples(tuples_1)

values_1 = [[9, 4, 3, 5], [9, 0, 5, 0], [3, 2, 8, 7], [6, 7, 1, 2]]
columns = ['a', 'b', 'c', 'd']

# Build the dataframe
df_1 = pd.DataFrame(values_1, columns=columns, index=index_1)
print(df_1 * 2)
print(type(df_1['a']))
print(len(df.columns))
print(df.shape)


