import requests
from pandas.io.json import json_normalize
import pandas as pd

# read json data from URL
url = "https://api.exchangerate-api.com/v4/latest/USD"
df = pd.read_json(url)
print(df.columns)
print(df.head())
print('***********************************')
print(df.loc['AED','rates'])
print(df.iloc[0])