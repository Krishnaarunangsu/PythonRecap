# Working with missing data
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(5, 3),
    index=['a', 'c', 'e', 'f', 'h'],
    columns=["one", "two", "three"]
)

print(f'The Original dataframe is:\n{df}')
print("*********************************************")

# Assigning a new column with default values
df["four"] = "bar"
print(f'The Modified  dataframe is:\n{df}')
print("*********************************************")

# Assigning a new column depending on the conditional check on another column
df["five"] = df["one"] > 0
print(f'The Modified  dataframe is:\n{df}')
print("*********************************************")

# Re-indexing the Dataframe
df_2=df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(f'The dataframe with the new index is:\n{df_2}')
print("*********************************************")

df_3=pd.DataFrame()
df_3["one"] = df_2["one"]
df_3["IS_NA"] = pd.isna(df_2["one"])
df_3["NOT_NA"]= df_2["one"].notna()

print(f'The new dataframe is:\n{df_3}')
print("*********************************************")


