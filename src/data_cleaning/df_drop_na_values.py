import pandas as pd
import numpy as np

df_1 = pd.DataFrame(
    {"name": ['Alfred', 'Batman', 'Catwoman'],
     "toy": [np.nan, 'Batmobile', 'Bullwhip'],
     "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT]}
)

print(f'The Original Dataframe is :\n{df_1}')
print('************************************************')

# Remove rows where at least one element is missing
df_without_NA=df_1.dropna()

print(f'The transformed  Dataframe is :\n{df_1.dropna()}')
print('************************************************')
print(f'The transformed  Dataframe is :\n{df_without_NA}')