# Drop Column in Dataframe


import pandas as pd

data = {"product_name": ["Keyboard", "Mouse", "Monitor", "CPU", "CPU", "Speakers", pd.NaT],
        "Unit_Price": [500, 200, 5000.235, 10000.550, 10000.550, 250.50, None],
        "No_Of_Units": [5, 5, 10, 20, 20, 8, pd.NaT],
        "Available_Quantity": [5, 6, 10, "Not Available", "Not Available", pd.NaT, pd.NaT],
        "Available_Since_Date": ['11/5/2021', '4/23/2021', '08/21/2021', '09/18/2021', '09/18/2021', '01/05/2021',
                                 pd.NaT]
        }

df = pd.DataFrame(data)
print(f'Original Dataframe:\n{df}')

# Drop the column at the index 2
print(f'Columns:\n{df.columns}')
print('***************************************')
print(f'Type of Object:\n{type(df.columns)}')
print('***************************************')
for i in df.columns:
    print(f'Column:{i}')

print('***************************************')
# print(f'Column Name:\n{df[]}')
for i in range(len(df.columns)):
    print(f'Index:{i} and Column Name:{df.columns[i]}')

print('***************************************')
# Drop the column by index
df.drop(columns=df.columns[2], axis=1, inplace=True)
print(f'Modified Dataframe:\n{df}')
print('***************************************')
# Drop the column by multiple indices
df.drop(columns=df.columns[[1, 2]], axis=1, inplace=True)
print(f'Modified Dataframe:\n{df}')

