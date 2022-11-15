# Convert the column type from string to datetime format in Pandas dataframe
import pandas as pd
import numpy as np

# Creating the dataframe
# Initializing the nested list with Data set
player_list = [['200712', 50000], ['200714', 51000], ['200716', 51500],
               ['200719', 53000], ['200721', 54000],
               ['200724', 55000], ['200729', 57000]]

# creating a pandas dataframe
df = pd.DataFrame(player_list, columns=['Dates', 'Patients'])

# printing dataframe
print(df)
print('########################')
# checking the type
print(df.dtypes)
print('********************************')

# converting the string to datetime format
df['Dates'] = pd.to_datetime(df['Dates'], format='%y%m%d')

# printing dataframe
print(df)
print('########################')
print(df.dtypes)