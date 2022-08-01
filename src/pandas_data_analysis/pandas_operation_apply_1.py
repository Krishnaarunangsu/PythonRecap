# pandas apply()
import numpy as np
import pandas as pd

df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
df_1 = pd.DataFrame([
    [4, 9],
    [4, 9],
    [4, 9]
], columns=['A', 'B'])

print(f'Original Dataframe:\n{df}')
print(df_1)

# Using a numpy universal function (in this case the same as np.sqrt(df)):
df_sq_root = df.apply(func=np.sqrt)
print(f'Dataframe Square Rooted:\n{df_sq_root}')
print(f'Original Dataframe:\n{df}')

# Using a reducing function on either axis
# Case I: axis =0: add corresponding elements row-wise
df_sum_row = df.apply(func=np.sum, axis=0)

print(f'Row-wise summation of the dataframe elements:\n{df_sum_row}')

# Case II: axis =1: add corresponding elements column-wise
df_sum_column = df.apply(func=np.sum, axis=1)

print(f'Column-wise summation of the dataframe elements:\n{df_sum_column}')
