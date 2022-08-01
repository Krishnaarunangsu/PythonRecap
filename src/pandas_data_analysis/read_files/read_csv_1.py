# Read csv file
import pandas as pd

df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")
print(f'Salaries CSV to pandas Dataframe:\n{df}')
