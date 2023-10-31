import pandas as pd
import numpy as np

data = {'first_set_of_numbers': [1, 2, 3, 4, 5, np.nan, 6, 7, np.nan, np.nan, 8, 9, 10, np.nan],
        'second_set_of_numbers': [11, 12, np.nan, 13, 14, np.nan, 15, 16, np.nan, np.nan, 17, np.nan, 19, np.nan],
        'third_set_of_numbers': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
                                 np.nan, np.nan, np.nan],
        'fourth_set_of_numbers': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
                                  np.nan,
                                  np.nan, np.nan, np.nan],
        'fifth_set_of_numbers': [20, 21, 22, 23, np.nan, 24, np.nan, 26, 27, np.nan, np.nan, 28, 29, 30]
        }
df = pd.DataFrame(data)

nan_present = df.isna().all()
print(f'Column NAN or not:\n{nan_present}')
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
if len(index_list_nan_cols) == 2:
    if index_list_nan_cols[0] + 1 == index_list_nan_cols[1]:
        X = df.iloc[:, 0:index_list_nan_cols[0]]
        # print(X)
        DF_list.append(X)
        print('**************************************************')
        Y = df.iloc[:, index_list_nan_cols[0] + 2:]
        # print(Y)
        DF_list.append(Y)

for DF in DF_list.__iter__():
    print(DF)
# print(nan_present)
# col_index_third_set = df.columns.get_loc('third_set_of_numbers')
# print(f'Index:{col_index_third_set}')

# print(df)
