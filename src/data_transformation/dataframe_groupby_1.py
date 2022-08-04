# Use groupby() function to group the data based on the “Team”
import numpy as np
import pandas as pd

# Making Dataframe from CSV file
df_nba = pd.read_csv("..\\..\\data\\csv\\nba.csv")

# applying groupby() function to group the data on team value.
print(df_nba['Team'].unique())
gk = df_nba.groupby('Team')

# Let's print the first entries
# in all the groups formed.
print(gk.first())
# var = df_nba.loc[df_nba['Team'] == 'Dallas Mavericks']
# print(var)

var_2 = df_nba[df_nba.isin(['Dallas Mavericks', 'Atlanta Hawks']).any(1)]
print(f'Dallas Mavericks and Alberta:\n{var_2}')
