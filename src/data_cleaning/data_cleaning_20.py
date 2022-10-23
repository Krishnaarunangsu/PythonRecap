import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "name": ['Alfred', 'Batman', 'Catwoman'],
        "toy": [np.nan, 'Batmobile', 'Bullwhip'],
        "born": [pd.NaT, pd.Timestamp("1940-04-25"),pd.NaT]
     }
)

print(f'The Original Dataframe is:\n{df}')
print('*************************************************')
# Case I: Drop the rows where at least one element is missing.
df_case_1 = df.dropna() # Remove all rows where at least one value is missing
print(f' The Case I Dataframe is:\n{df_case_1}')
print('*************************************************')
# df.dropna(inplace=True) #inplace=True refers to the effect in the same dataframe
# print(f' The Case I Dataframe with inplace=True is:\n{df}')

# Case II : Drop the columns where at least one element is missing.
df_case_2 = df.dropna(axis=1)
# df_case_2 = df.dropna(axis='columns')
print(f' The Case II Dataframe is:\n{df_case_2}')
print('*************************************************')

# Case III : Drop the rows where all elements are missing.
df_case_3 = df.dropna(how='all')
print(f' The Case III Dataframe is:\n{df_case_3}')

# Case IV: Keep only the rows with at least 2 non-NA values.
df_case_4= df.dropna(thresh=2)
print(f' The Case IV Dataframe is:\n{df_case_4}')

# Case V: Define in which columns to look for missing values.
df_case_5=df.dropna(subset=['name', 'toy'])
print(f' The Case V Dataframe is:\n{df_case_5}')

# Case VI: Keep the DataFrame with valid entries in the same variable.
df.dropna(inplace=True)
print(f' The Case VI Dataframe is:\n{df}')