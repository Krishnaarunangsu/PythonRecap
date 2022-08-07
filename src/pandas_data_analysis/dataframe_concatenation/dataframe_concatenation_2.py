# Concatenation of Dataframes
import pandas as pd

# Dataframe-1
df1 = pd.DataFrame(
    {
        "A_1": ["A0", "A1", "A2", "A3"],
        "B_1": ["B0", "B1", "B2", "B3"],
        "C_1": ["C0", "C1", "C2", "C3"],
        "D_1": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)

print(f'Dataframe-1:\n{df1}')

# Dataframe-2
df2 = pd.DataFrame(
    {
        "A_2": ["A4", "A5", "A6", "A7"],
        "B_2": ["B4", "B5", "B6", "B7"],
        "C_2": ["C4", "C5", "C6", "C7"],
        "D_2": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)

print(f'Dataframe-2:\n{df2}')

# Dataframe-3
df3 = pd.DataFrame(
    {
        "A_3": ["A8", "A9", "A10", "A11"],
        "B_3": ["B8", "B9", "B10", "B11"],
        "C_3": ["C8", "C9", "C10", "C11"],
        "D_3": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)

print(f'Dataframe-3:\n{df3}')

frames = [df1, df2, df3]

# Concatenate the Dataframes
concatenated_Dataframes = pd.concat(frames)

print(f'Concatenated Dataframes:\n{concatenated_Dataframes}')
