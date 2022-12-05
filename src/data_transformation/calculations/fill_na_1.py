import pandas as pd
import numpy as np

df_1 = pd.DataFrame(
    np.random.randn(5, 3),
    index=['a', 'c', 'e', 'f', 'h'],
    columns=["one", "two", "three"]
)

print(f'The original Dataframe is:\n{df_1}')

df_1["four"] = "bar"

print(f'The modified Dataframe is:\n{df_1}')

df_1.loc[['a', 'c', 'h'], "one"] = np.nan

print(f'The modified Dataframe is:\n{df_1}')

df_1["five"] = df_1["one"].isna()

print(f'The modified Dataframe is:\n{df_1}')

df_1["Timestamp"] = pd.Timestamp("2012-01-01")

print(f'The modified Dataframe is:\n{df_1}')

df_1.loc[['a', 'c', 'h'], "Timestamp"] = pd.NaT

print(f'The modified Dataframe is:\n{df_1}')
df_2 = df_1
# df_1.fillna(0


df_1["one"].fillna("missing", inplace=True)
print(f'The modified Dataframe is:\n{df_2}')

df_1["one"][df_1["one"] == "missing"] = 0
print(f'The modified Dataframe is:\n{df_2}')

df_1.fillna(0, inplace=True)
print(f'The modified Dataframe is:\n{df_2}')

