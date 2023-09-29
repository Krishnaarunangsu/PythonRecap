import pandas as pd

dataset = {'toothed': [1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
           'hair': [1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
           'breathes': [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
           'legs': [1, 1, 0, 1, 1, 1, 0, 0, 1, 1],
           'species': [1, 1, 0, 1, 1, 1, 0, 0, 1, 0]
           }

df = pd.DataFrame(dataset)
print(df)
print('**************************************************')
X = df.iloc[:, 0:df.columns.get_loc('legs')]
print(X)
print('**************************************************')
Y = df.iloc[:, df.columns.get_loc('legs') + 1:]
print(Y)

# df.head()
