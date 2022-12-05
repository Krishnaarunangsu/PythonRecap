import pandas as pd
import numpy as np

# Create a dataframe
df_1 = pd.DataFrame({"A": [2, 3, 8, 14],
                     "B": [1, 2, 4, 3],
                     "C": [5, 3, 9, 2]})

print(f'The Original Data frame is:\n{df_1}')
print('*********************************************')
# Computing sum over Index axis
print(f'Cumulative sum over Index axis:\n{df_1.cumsum(axis=0)}')
print('*********************************************')
# Create a dataframe
df_2 = pd.DataFrame({"A": [None, 3, 8, 14],
                     "B": [1, None, 4, 3],
                     "C": [5, 3, 9, None]})

print(f'The Original Data frame is:\n{df_2}')
print('*********************************************')
# Computing sum over Index axis skip NA = True
print(df_2.cumsum(axis=0, skipna=True))
print('*********************************************')
# Computing sum over Index axis skip NA = False
print(df_2.cumsum(axis=0, skipna=False))
