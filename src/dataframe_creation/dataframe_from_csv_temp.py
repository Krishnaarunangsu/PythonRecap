# Python program to illustrate
# creating a data frame using CSV files

# import pandas module
import pandas as pd

df=None
# creating a data frame
df = pd.read_csv("C://Arunangsu//AI//Data//archive//CardioGoodFitness.csv")
print(df.head())


if df is not None:
    print(df.head())

