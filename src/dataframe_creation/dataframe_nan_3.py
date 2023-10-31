import pandas as pd
import numpy as np

df=None
# creating a data frame
try:
    # df = pd.read_csv("CardioGoodFitness.csv")
    df = pd.read_csv("C://Arunangsu//AI//Data//archive//CardioGoodFitness_blank_4.csv")
    print(df.head())
    print('**********************************************************')
except FileNotFoundError as fe:
    print(f'Error:{fe}')
    print(f'Error:{fe.args}')
    print(f'File Name:{fe.filename}')
    print('**********************************************************')
    # print(f'Error:{fe.with_traceback()}')

if df is not None:
    print(df.head())
nan_present = df.isna().all()
print(f'Column NAN or not:\n{nan_present}')
print('**********************************************************')
# print(f'Data Type of nan_present:\n{type(nan_present)}')
index_list_nan_cols = []
for item in nan_present.items():
    # print(item[1])
    if item[1]:
        print(f'The Column Name with all NAN:{item[0]}')
        print(f'The Column Index of column with all NAN:{df.columns.get_loc(item[0])}')
        index_list_nan_cols.append(df.columns.get_loc(item[0]))

print(index_list_nan_cols)
DF_list = list()

# If there are more than two columns or fewer than 2 columns with NAN values it will not work
if len(index_list_nan_cols) == 2:
    # if the two NAN columns are consecutive columns then it will work
    if index_list_nan_cols[0] + 1 == index_list_nan_cols[1]:
        # if the last two columns have NAN values then nothing to do
        if index_list_nan_cols[0] != len(df.columns)-2:
            X = df.iloc[:, 0:index_list_nan_cols[0]]
            # print(X)
            DF_list.append(X)
            print('**************************************************')
            Y = df.iloc[:, index_list_nan_cols[0] + 2:]
            # print(Y)
            DF_list.append(Y)

if len(DF_list)!=0:
    for DF in DF_list.__iter__():
        print(DF)
        print('**********************************************************')
# print(nan_present)
# col_index_third_set = df.columns.get_loc('third_set_of_numbers')
# print(f'Index:{col_index_third_set}')

# print(df)
