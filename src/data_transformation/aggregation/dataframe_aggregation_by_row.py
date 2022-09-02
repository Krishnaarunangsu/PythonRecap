# Aggregate ‘sum’ and ‘min’ function across all the columns in data frame.
import numpy as np
import pandas as pd

df_1 = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [np.nan, np.nan, np.nan]
],
    columns=['A', 'B', 'C']
)

print(f'Dataframe-1:\n{df_1}')
print('***************************************************')

# Aggregate these functions over the rows.
aggregation_result = df_1.agg(['sum', 'min'])
print(f'Aggregation Result by Row:\n{aggregation_result}')
