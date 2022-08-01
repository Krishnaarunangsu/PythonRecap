import pandas as pd

df = pd.DataFrame(
    [
     [0, 2, 3],
     [0, 4, 1],
     [10, 20, 30]
    ],
    index=[4, 5, 6],
    columns=['A', 'B', 'C']
)

print(f'Dataframe:\n{df}')

# Homogeneous  Index
print(f'Dataframe Index/Rows: {df.index}')
print(f'Dataframe Columns: {df.columns}')
