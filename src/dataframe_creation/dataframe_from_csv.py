# Python program to illustrate
# creating a data frame using CSV files

# import pandas module
import pandas as pd

df=None
# creating a data frame
try:
    #df = pd.read_csv("CardioGoodFitness.csv")
    df = pd.read_csv("C://Arunangsu//AI//Data//archive//CardioGoodFitness.csv")
    print(df.head())
except FileNotFoundError as fe:
    print(f'Error:{fe}')
    print(f'Error:{fe.args}')
    print(f'File Name:{fe.filename}')
    # print(f'Error:{fe.with_traceback()}')

if df is not None:
    print(df.head())

