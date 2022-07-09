import pandas as pd

df = pd.DataFrame({
    'names': ['Jane', 'John', 'Ashley', 'Max', 'Emily', 'Black'],
    'A': [1.0, 8.0, 6.0, 0.0, 7.0, 3.0],
    'B': [6.0, 1.0, 3.0, 3.0, 6.0, 3.0],
    'C': [6.0, 2.0, 5.0, 4.0, 6.0, 4.0],
    'D': [9.0, 8.0, 1.0, 0.0, 0.0, 5.0],
    'E': [1.0, 8.0, 7.0, 8.0, 6.0, 1.0]
})
print(f'Original Data:\n{df}')

# The loc function specifies rows and columns with their labels.
# The [5, :] expression indicates row with label 5 and all columns.

print(f' 5th Row-Label 5:\n{df.loc[5, :]}')
print(type(df.loc[5, :]))

# The drop function with axis parameter set to zero can be used to drop a row.
df = df.drop(index=5, axis=0)

print(f'Modified Dataframe:\n{df}')
df.loc[5] = [8.0, 7.0, 0.0, 5.0, 4.0, 2.0]
print(f'Modified Dataframe:\n{df}')
