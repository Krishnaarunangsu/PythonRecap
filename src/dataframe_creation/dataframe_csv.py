import pandas as pd

df = pd.read_csv('nba.csv')
print(df.describe())
print('****************************')
print(df.info)
