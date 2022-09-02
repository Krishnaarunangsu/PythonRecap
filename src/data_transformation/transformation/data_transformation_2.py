# Even though the resulting DataFrame must have the same length as the input DataFrame,
# it is possible to provide several input functions:

import numpy as np
import pandas as pd

# Create a pandas Series
df = pd.Series(range(3))
print(f'Original Data:\n{df}')
print(type(df))

# Apply Transformation and get a Dataframe
df = df.transform([np.sqrt, np.exp])
print(f'Modified Data:\n{df}')
print(type(df))
