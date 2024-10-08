# Joining the Dataframe: Join DataFrames using their indexes.
import pandas as pd

# Dataframe-1
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

# Dataframe-2
print(f'Dataframe-2:\n{df_2}')

# Join Dataframe df2 with Dataframe 1
dataframe_joined = df_1.join(other=df_2, lsuffix='_caller', rsuffix='_other')
print(f'Dataframes after joining:\n{dataframe_joined}')
