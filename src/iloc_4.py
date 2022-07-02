import pandas as pd
import numpy as np

mydict = [{'product': 'A', 'month': 'Jan', 'sold': 85},
          {'product': 'A', 'month': 'Feb', 'sold': 200},
          {'product': 'A', 'month': 'Mar', 'sold': 180},
          {'product': 'B', 'month': 'Jan', 'sold': 90},
          {'product': 'B', 'month': 'Feb', 'sold': 80},
          {'product': 'B', 'month': 'Mar', 'sold': 130}
          ]

sales = pd.DataFrame(mydict)
print(sales)

pick = np.logical_or(sales['product'] == 'B',
                     sales['sold'] < 100)

print(pick)
print(sales[pick])
