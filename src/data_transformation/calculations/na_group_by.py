# NA groups in GroupBy are automatically excluded.
import pandas as pd
import numpy as np
from pandas import DataFrame

df_1: DataFrame = pd.DataFrame(np.random.randn(5, 3),
                               index=["a", "c", "e", "f", "h"],
                               columns=["one", "two", "three"],
                               )

print(f'The Original Dataframe df_1 is:\n{df_1}')
print('*************************************************')
df_1.loc[['a', 'c', 'h'], 'one']=np.nan
print(f'The Modified Dataframe df_1 is:\n{df_1}')

# Calculate the mean of the column "one"
print(df_1.groupby("one").mean())
