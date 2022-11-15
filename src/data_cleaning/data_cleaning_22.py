import pandas as pd
import numpy as np

series_1 = pd.Series([1, 2, 3])
print(f'{series_1.loc[0]}')

series_1.loc[0]=np.nan
print(f'{series_1.loc[0]}')