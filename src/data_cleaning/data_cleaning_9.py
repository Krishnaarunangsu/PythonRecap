# Drop Rows that Contain Values in a List

import pandas as pd

# Create dataframe with 4 columns
data = pd.DataFrame({
    "name": ['sravan', 'jyothika', 'harsha', 'ramya',
             'sravan', 'jyothika', 'harsha', 'ramya',
             'sravan', 'jyothika', 'harsha', 'ramya'],
    "subjects": ['java', 'java', 'java', 'python',
                 'python', 'python', 'html/php', 'html/php',
                 'html/php', 'php/js', 'php/js', 'php/js'],
    "marks": [98, 79, 89, 97, 82, 98, 90,
              87, 78, 89, 93, 94]
})

# display
print(f'Original Dataframe:\n{data}')

# List of marks to be excluded from the above data
marks_to_be_excluded = [98, 82, 79]

print('********************************')
# drop rows where value is 98 by using List and Boolean
dataframe_cleaned_1 = data[data.marks.isin(marks_to_be_excluded) == False]
print(f'Cleaned Data:\n{dataframe_cleaned_1}')
