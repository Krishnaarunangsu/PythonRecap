import pandas as pd

my_dict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
my_df = pd.DataFrame(my_dict)
print(my_df)

# Indexing just the rows

# With a scalar integer.
print(type(my_df.iloc[0]))
print(my_df.iloc[0])

# With a list of integers.
print(type(my_df.iloc[[0]]))
print(my_df.iloc[[0]])
print(my_df.iloc[[0, 1]])

# Indexing both axes
# You can mix the indexer types for the index and columns. Use : to select the entire axis.
print(my_df.iloc[(0, 0)])
print(my_df.iloc[(0, 1)])
print(my_df.iloc[0, 1])

# With a slice object.
print(my_df.iloc[:3])

# With a boolean mask the same length as the index.
print(my_df.iloc[[True, False, True]])

print(my_df)
# With lists of integers.
print(my_df.iloc[[0, 1]])
print(my_df)
# With lists of integers.
print(my_df.iloc[[0, 1], [1, 3]])

# With slice objects.
print(my_df.iloc[1:3, 0:3])

# With a boolean array whose length matches the columns.
print(my_df.iloc[:, [True, False, True, False]])

# With a callable function that expects the Series or DataFrame.
print(my_df.iloc[:, [0, 2]])
print(my_df.iloc[:, lambda df:[0, 2]])
