# Joining the Dataframe: If we want to join using the key columns, we need to set key to be
# the index in both df and other. The joined DataFrame will have key as its index.
import pandas as pd

df_1 = pd.DataFrame(
    {
        'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
        'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']
    }
)

print(f'Dataframe-1:\n{df_1}')

df_2 = pd.DataFrame(
    {
        'key': ['K0', 'K1', 'K2'],
        'B': ['B0', 'B1', 'B2']
    }
)

print(f'Dataframe-2:\n{df_2}')

dataframe_joined = df_1.set_index('key').join(df_2.set_index('key'))
print(f'Dataframes after joining:\n{dataframe_joined}')
