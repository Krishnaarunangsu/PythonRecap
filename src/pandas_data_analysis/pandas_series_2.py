import pandas as pd

r = [1, 2]
ser = pd.Series(r, copy=False)
print(ser)
print(ser.iloc[0])
print(ser.loc[0])

ser = pd.Series(r, index=['Y', 'Z'], copy=False)
print(ser)
print(ser.iloc[0])
print(ser.loc['Y'])
