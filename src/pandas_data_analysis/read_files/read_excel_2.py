# Reading an Excel File in Pandas
import pandas as pd

# df_excel_employee = pd.read_excel("../../../data/excel/records.xlsx", sheet_name='Employees')
# print(f'Employees Dataframe:\n{df_excel_employee}')
# print(f'Columns of the Employee Dataframe:{df_excel_employee.columns.ravel()}')
# print(f'Columns of the Employee Dataframe:{df_excel_employee.columns}')
#
# Printing a Column Data
# print(f'Data of the EmpName Column:\n{df_excel_employee["EmpName"]}')
# print(f'Data of the EmpName Column:\n{df_excel_employee["EmpName"].tolist()}')

# Pandas read_excel() usecols example
# We can specify the column names to be read from the excel file.
# It’s useful when you are interested in only a few of the columns of the excel sheet.
df_excel_car = pd.read_excel("../../../data/excel/records.xlsx", sheet_name='Cars', usecols=['Car Name', 'Car Price'])

print(f'Car Dataframe:\n{df_excel_car}')

