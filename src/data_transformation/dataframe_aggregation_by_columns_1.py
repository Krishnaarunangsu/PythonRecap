# Aggregate ‘sum’ and ‘min’ function across all the columns in data frame individually.
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

# Aggregate different functions over the columns and rename the index of the resulting DataFrame.
aggregation_result = df_1.agg(x=('A', max), y=('B', min), z=('C', np.mean))
print(f'Aggregation Result by Individual Column:\n{aggregation_result}')
