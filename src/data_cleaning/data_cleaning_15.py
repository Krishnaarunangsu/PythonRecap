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

# Selecting duplicate rows except first occurrence based on all columns
duplicate_emp_data = employee_data[employee_data.duplicated(keep='first')]

# Print the resultant Dataframe
print(f"Duplicate Rows of employee data:\n{duplicate_emp_data}")

for i in duplicate_emp_data.index:
    print(f'Duplicate data exists in:{i} row')



