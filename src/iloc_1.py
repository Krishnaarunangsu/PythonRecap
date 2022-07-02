import pandas as pd

my_dict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]

print(my_dict)

df = pd.DataFrame(my_dict)
print(df)

# Indexing the rows
# Case I: with a scalar integer
print(type(df.iloc[0]))
print(df.iloc[0])

# Case II: with a list of integers
print(df.iloc[[0]])
print(df.iloc[[0, 1]])
print(df.iloc[[1, 2]])
print(df.iloc[[1, 2], [2]])

# Case III: with a slice object
print(df.iloc[:3])

# Case IV:With a boolean mask the same length as the index
print(df.iloc[[True, False, True]])

# Case V: With a callable, useful in method chains. The x passed to the lambda is the DataFrame being sliced. This
# selects the rows whose index label even.
print(df.iloc[lambda x: x.index % 2 == 0])
