import pandas as pd

# List of Tuples
employees = [('Stuti', 28, 'Varanasi'),
             ('Saumya', 32, 'Delhi'),
             ('Aaditya', 25, 'Mumbai'),
             ('Saumya', 32, 'Delhi'),
             ('Saumya', 32, 'Delhi'),
             ('Saumya', 32, 'Mumbai'),
             ('Aaditya', 40, 'Dehradun'),
             ('Seema', 32, 'Delhi')
             ]
# Creating a DataFrame object
employee_data = pd.DataFrame(employees, columns=['Name', 'Age', 'City'])

print(employee_data)

# Selecting duplicate rows based on list of column names
df_employee_duplicate = employee_data[employee_data.duplicated(['Name', 'Age'], keep=False)]
print(f'Duplicate rows based on "City" column all the entries:\n{df_employee_duplicate}')

# Selecting duplicate rows based on list of column names
df_employee_duplicate = employee_data[employee_data.duplicated(['Name', 'Age'])]
print(f'Duplicate rows based on "City" column:\n{df_employee_duplicate}')

# For Tutorial Preparation:
# https://www.geeksforgeeks.org/find-duplicate-rows-in-a-dataframe-based-on-all-or-selected-columns/
# For More Practice:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html
# https://thispointer.com/pandas-find-duplicate-rows-in-a-dataframe-based-on-all-or-selected-columns-using-dataframe-duplicated-in-python/
# https://appdividend.com/2022/06/25/how-to-find-duplicate-rows-in-pandas-dataframe/
# https://www.machinelearningplus.com/pandas/pandas-duplicated/
# https://edu.machinelearningplus.com/s/store
