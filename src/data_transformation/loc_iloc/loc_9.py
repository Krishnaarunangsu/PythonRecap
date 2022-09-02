import pandas as pd

# Getting values on a DataFrame with an index that has integer labels
# Another example using integers for the index

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=[7, 8, 9], columns=['max_speed', 'shield'])

print(df)

# Slice with integer labels for rows. As mentioned above,
# note that both the start and stop of the slice are included.
print(df.loc[7:])
print(df.loc[7:9])
