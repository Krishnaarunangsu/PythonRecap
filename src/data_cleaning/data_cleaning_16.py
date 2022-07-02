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

# Selecting duplicate rows based on "City" column
df_employee_duplicate = employee_data[employee_data.duplicated('City', keep=False)]
print(f'Duplicate rows based on "City" column all the entries:\n{df_employee_duplicate}')

# Selecting duplicate rows based on "City" column
df_employee_duplicate = employee_data[employee_data.duplicated('City')]
print(f'Duplicate rows based on "City" column:\n{df_employee_duplicate}')
