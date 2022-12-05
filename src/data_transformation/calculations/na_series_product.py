# The product of an empty or all-NA Series or column of a DataFrame is 1.
import numpy as np
import pandas as pd

print(pd.Series([np.nan]).prod())
print(pd.Series([], dtype="float64").prod())
