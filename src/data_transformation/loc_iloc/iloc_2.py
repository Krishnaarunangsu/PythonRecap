import pandas as pd

mydict = [{'s_length': 5.1, 's_width': 3.5, 'species': 'setosa'},
          {'s_length': 7.0, 's_width': 3.2, 'species': 'versicolor'},
          {'s_length': 5.1, 's_width': 3.5, 'species': 'virginica'}]

df = pd.DataFrame(mydict)
print(df)
print(df.iloc[0, [0]])
print(df.iloc[[0, 1], [0]])
