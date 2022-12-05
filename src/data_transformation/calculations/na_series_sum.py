# The sum of an empty or all-NA Series or column of a DataFrame is 0.
import numpy as np
import pandas as pd

print(pd.Series([np.nan]).sum())
print(pd.Series([], dtype="float64").sum())
