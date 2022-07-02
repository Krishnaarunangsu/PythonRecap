# Drop rows that contain specific values in multiple columns
# import pandas module
import pandas as pd

# create dataframe with 4 columns
data = pd.DataFrame({

    "name": ['sravan', 'jyothika', 'harsha', 'ramya',
             'sravan', 'jyothika', 'harsha', 'ramya',
             'sravan', 'jyothika', 'harsha', 'ramya'],
    "subjects": ['java', 'java', 'java', 'python',
                 'python', 'python', 'html/php',
                 'html/php', 'html/php', 'php/js',
                 'php/js', 'php/js'],
    "marks": [98, 79, 89, 97, 82, 98, 90,
              87, 78, 89, 93, 94]
})

print(f'Original Data:\n{data}')

# drop specific values:
# where marks is 98 and name is sravan
df_new_1 = data[(data.marks != 98) & (data.name != "sravan")]
print(f'Cleaned Data by condition "&":\n{df_new_1}')

# drop specific values
# where marks is 98 or name is sravan
df_new_2 = data[(data.marks != 98) | (data.name != 'sravan')]
# data[(data.marks != 98) | (data.name != "sravan")]
# data[(data.marks != 98) | (data.name != 'sravan')]
print(f'Cleaned Data by condition "or":\n{df_new_2}')

df_sravan = data.query("name.eq('sravan')")
print(df_sravan)

df_not_sravan = data.query("name.ne('sravan')")
print(df_not_sravan)
