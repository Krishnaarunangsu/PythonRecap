import pandas as pd
import numpy as np

# Create a dataframe
df_1 = pd.DataFrame({"A": [2, 3, 8, 14],
                     "B": [1, 2, 4, 3],
                     "C": [5, 3, 9, 2]})    

print(f'The Original Data frame is:\n{df_1}')
print('*********************************************')
# Computing sum over Columns
print(f'Cumulative sum over Index axis:\n{df_1.cumsum(axis=1)}')
print('*********************************************')
