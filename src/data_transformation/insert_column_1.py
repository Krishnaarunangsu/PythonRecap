# Insert column in a dataframe in the specific position

# import the library
import pandas as pd
import numpy as np

# Create an empty Dataframe
df = pd.DataFrame()

print(f'Index of the Dataframe:\n{df.index}')

# Insert a column at the index 0
df.insert(loc=0, column='new', value=np.random.random(5))
print(f'The modified Dataframe is:\n{df}')
