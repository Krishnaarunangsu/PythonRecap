# Convert the column type from string to datetime format in Pandas dataframe
import pandas as pd
import numpy as np

# Creating the dataframe
df_1 = pd.DataFrame(
    {'Date': ['11/18/2011', '04/23/2008', '10/02/2019'],
     'Event': ['Music', 'Poetry', 'Theatre'],
     'Cost': [10000, 5000, 15000]
     }
)

print(f'The original Dataframe is:\n{df_1}')
print('#########################################')
print(f'The Column dTypes are:\n{df_1.dtypes}')
print('************************************************')

# Convert the Date Column to datetime type
df_1['Date']=pd.to_datetime(df_1['Date'])
print(f'The Modified Dataframe is:\n{df_1}')
print('#########################################')
print(f'The Column dTypes are:\n{df_1.dtypes}')
