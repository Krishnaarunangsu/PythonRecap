import pandas as pd
from IPython.display import display

data = pd.DataFrame({'MONTH': ['JAN', 'FEB'],
                     'day': [7, 8],
                     'year': [2015, 2015],
                     'session_id': [17357, 10011]})

display(data)
for j, p in data.iterrows():
    data.loc[j, 'year'] = p['MONTH'].lower()

print(data)
