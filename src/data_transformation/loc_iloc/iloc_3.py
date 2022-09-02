import pandas as pd

mydict = [{'a': 2, 'b': 1, 'c': 14},
          {'a': 7, 'b': 5, 'c': 3},
          {'a': 12, 'b': 8, 'c': 6}]

df = pd.DataFrame(mydict)
print(df)
print(df['a'])
