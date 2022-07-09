# Drop Column in Dataframe


import pandas as pd

data = {"product_name": ["Keyboard", "Mouse", "Monitor", "CPU", "CPU", "Speakers", pd.NaT],
        "Unit_Price": [500, 200, 5000.235, 10000.550, 10000.550, 250.50, None],
        "No_Of_Units": [5, 5, 10, 20, 20, 8, pd.NaT],
        "Available_Quantity": [5, 6, 10, "Not Available", "Not Available", pd.NaT, pd.NaT],
        "Available_Since_Date": ['11/5/2021', '4/23/2021', '08/21/2021', '09/18/2021', '09/18/2021', '01/05/2021',
                                 pd.NaT],
        "Type": [pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT]
        }
df = pd.DataFrame(data)
print(df)

# how="any" or how="all
df.dropna(axis=1, how='all', inplace=True)
print(df)
