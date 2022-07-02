import pandas as pd

my_dict = [{'ID': 1, 'VIEWS': 1000, 'CLICKS': 300},
           {'ID': 2, 'VIEWS': 1200, 'CLICKS': 800},
           {'ID': 3, 'VIEWS': 800, 'CLICKS': 500}, ]

print(my_dict)

df = pd.DataFrame(my_dict)
print(df)
print(df.iloc[[1, 2]])
