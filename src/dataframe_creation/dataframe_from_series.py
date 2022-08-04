# Create Dataframe from Series

import pandas as pd

# Initialize data to series
data = pd.Series([10, 20, 30, 40])
print(f'The Pandas Series is:\n{data}')
print('***********************************************')
# Create the Dataframe
dataframe_1 = pd.DataFrame(data)

print(f'Dataframe from the Series:\n{dataframe_1}')
print(f'Dataframe dtype:{dataframe_1.dtypes}')
