import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 8, 6, 0, 7],
    'B': [6, 1, 3, 3, 6],
    'C': [6, 2, 5, 4, 6],
    'D': [9, 8, 1, 0, 0],
    'E': [1, 8, 7, 8, 6]
})

print(f'Original Data:\n{df}')

# Add New Column
df['new'] = np.random.random(5)
print(f'Data after added column:\n{df}')

# Drop a column
# df.drop('new', axis=1)

df.drop('new', axis=1, inplace=True)  # inplace=True updates the original Dataframe
print(f'Data after deleting the column new:\n{df}')
