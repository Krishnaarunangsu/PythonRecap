# Use bfill() function to populate missing values na values in the series across column
import pandas as pd

series_1 = pd.Series([1, 2, 3, 4, 5])
print(f'Original Series:\n{series_1}')
series_2 = series_1.replace(to_replace=[1, 2], method='bfill')
print(f'Modified Series after backfill:\n{series_2}')
series_3 = series_1.replace(to_replace=[4, 5], method='ffill')
print(f'Modified Series after frontfill:\n{series_3}')
