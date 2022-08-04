# Create Dataframe from Series

import pandas as pd

# Initialize data to series
data_1 = pd.Series([10, 20, 30, 40])
data_2 = pd.Series([7, 3, 5, 2])
print(f'Series-1 is:\n{data_1}')
print(f'Series-2 is:\n{data_2}')

# Data as dict
data = {
         'A': data_1,
         'B': data_2
       }
print('***********************************************')
# Create the Dataframe
dataframe_1 = pd.DataFrame(data)

print(f'Dataframe from the Series:\n{dataframe_1}')
print(f'Dataframe dtype:\n{dataframe_1.dtypes}')
