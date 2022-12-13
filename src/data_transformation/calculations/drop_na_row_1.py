import pandas as pd
import numpy as np

df_1 = pd.DataFrame(
    np.random.randn(5, 2),
    index=['a', 'c', 'e', 'f', 'h'],
    columns=["two", "three"]
)
df_1["one"] = np.nan
print(df_1)
column_reposition = df_1.pop("one")
df_1.insert(0, column_reposition.name, column_reposition)
print(df_1)

# Remove any row with at least one NaN
# df_1.dropna(axis=0, inplace=True)
df_2 = df_1.dropna(axis=0)
print(df_2)

# Remove any column with at least one NaN
df_3 = df_1.dropna(axis=1)
print(df_3)
