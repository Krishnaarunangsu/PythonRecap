# Reading an Excel File in Pandas
import pandas as pd

# Read the Employees Sheet of thw records.xlsx
df_excel_employee = pd.read_excel("../../../data/excel/records.xlsx", sheet_name='Employees')

# Read the Cars Sheet of the records.xlsx
df_excel_car = pd.read_excel("../../../data/excel/records.xlsx", sheet_name='Cars')

# If no sheet name is specified then the first sheet in the excel is read by default
df_1 = pd.read_excel("..\\..\\..\\data\\excel\\records.xlsx")

print(f'Employees Dataframe:\n{df_excel_employee}')
print('***********************************************************')
print(f'Car Dataframe:\n{df_excel_car}')

