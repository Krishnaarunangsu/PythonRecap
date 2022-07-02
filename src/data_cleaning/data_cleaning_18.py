import pandas as pd

# technology dictionary
technologies = {
    'Courses': ["Spark", "PySpark", "Python", "pandas", "Python", "Spark", "pandas"],
    'Fee': [20000, 25000, 22000, 30000, 22000, 20000, 30000],
    'Duration': ['30days', '40days', '35days', '50days', '40days', '30days', '50days'],
    'Discount': [1000, 2300, 1200, 2000, 2300, 1000, 2000]
}
df = pd.DataFrame(technologies)
print(df)

# Below are quick examples

# Select duplicate row based on all columns
df2 = df[df.duplicated(keep=False)]
print(f'Duplicated Rows except based on all columns:\n{df2}')

# Select duplicate rows except first occurrence based on all columns
df2 = df[df.duplicated()]
print(f'Duplicated Rows except first occurrence based on all columns:\n{df2}')

# Get duplicate last rows based on all columns
df2 = df[df.duplicated(keep='last')]
print(f'Duplicated Rows except last occurrence based on all columns:\n{df2}')

# Get list Of duplicate rows using single columns
df2 = df[df['Courses'].duplicated() == True]
print(f'Duplicated Rows based on single column:\n{df2}')

# Get list of duplicate rows based on 'Courses' column
df2 = df[df.duplicated('Duration')]
print(f'Duplicated Rows based on "Duration" column:\n{df2}')

# Get list Of duplicate rows using multiple columns
df2 = df[df[['Courses', 'Fee', 'Duration']].duplicated() == True]
print(f'Duplicated Rows using multiple columns:\n{df2}')

# Get list of duplicate rows based on list of column names
df2 = df[df.duplicated(['Courses', 'Fee', 'Duration'])]
print(f'Duplicated Rows based on multiple columns:\n{df2}')

# For detailed studies:
# https://sparkbyexamples.com/pandas/pandas-get-list-of-all-duplicate-rows/
