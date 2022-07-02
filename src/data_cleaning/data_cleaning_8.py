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

print('********************************')
# drop rows where value is 98 by using not equal operator: !=
dataframe_cleaned_1 = data[data.marks != 98]
print(f'Cleaned Data:\n{dataframe_cleaned_1}')

print('********************************')
# drop rows where value is 98 by using not equal operator: ne
dataframe_cleaned_2 = data.query("marks.ne(98)")
print(f'Cleaned Data:\n{dataframe_cleaned_2}')
