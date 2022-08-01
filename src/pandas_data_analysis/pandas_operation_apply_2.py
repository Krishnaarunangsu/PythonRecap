# pandas apply()
# Documentation: https://www.geeksforgeeks.org/applying-lambda-functions-to-pandas-dataframe/
import numpy as np
import pandas as pd

# creating and initializing a nested list
values_list = [[15, 2.5, 100], [20, 4.5, 50], [25, 5.2, 80],
               [45, 5.8, 48], [40, 6.3, 70], [41, 6.4, 90],
               [51, 2.3, 111]]
columns = ['Field_1', 'Field_2', 'Field_3']
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

df = pd.DataFrame(values_list, columns=columns, index=index)
print(f'Original Dataframe:\n{df}')

# Apply function numpy.square() to square the values of one row only i.e. row
# with index name 'd'
df_transformed = df.apply(lambda x: np.square(x) if x.name == 'd' else x, axis=1)
print(f'Dataframe Transformed:\n{df_transformed}')

df_column_transformed = df.apply(lambda x: x + 10)
print(f'Column Transformed:\n{df_column_transformed}')
