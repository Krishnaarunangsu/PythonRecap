# Reading an Excel File in Pandas
import pandas as pd

df_excel_employee = pd.read_excel("../../../data/excel/records.xlsx", sheet_name='Employees')
df_excel_car = pd.read_excel("../../../data/excel/records.xlsx", sheet_name='Cars')
df_1 = pd.read_excel("..\\..\\..\\data\\excel\\records.xlsx")
print(f'Employees Dataframe:\n{df_excel_employee}')
print(f'Car Dataframe:\n{df_excel_car}')
# print(f'Columns of the Employee Dataframe:{df_excel_employee.columns.ravel()}')
print(f'Columns of the Employee Dataframe:{df_excel_employee.columns}')

# Printing a Column Data
print(f'Data of the EmpName Column:\n{df_excel_employee["EmpName"]}')
print(f'Data of the EmpName Column:\n{df_excel_employee["EmpName"].tolist()}')
