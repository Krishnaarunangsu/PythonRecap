import pandas as pd
import pandas as pd

df = pd.DataFrame({'A': [11, 21, 31],
                   'B': [12, 22, 32],
                   'C': [13, 23, 33]},
                  index=['ONE', 'TWO', 'THREE'])

print(df)

stores = pd.DataFrame({'X': [10, 15, 12],
                       'Y': [20, 15, 50],
                       'Cost': [20, 18, 30],
                       'Distance': [23, 21, 51]},
                      index=['a', 'b', 'c']
                      )

print(stores.loc[['a', 'b']])