import pandas as pd

df = pd.read_csv("..\\..\\data\\flights_tickets_serp2018-12-16.csv")

print(f'Dataframe Columns:\n{df.columns}')
print('*********************************************')
print(f'Dataset Structure:\n{df.info()}')
print('*********************************************')
print(f'Dataframe Data types:{type(df.dtypes)}')
print(f'Dataframe Summary:{df.head()}')

symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',
           '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
# print(symbols)

print(f'Contents of the title column:\n{df["title"]}')

# Retained '.' and '$'
spec_chars = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%',
              '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '_', '=', ']',
              '!', '>', ';', '?', '#', ')', '/'}

for char in spec_chars:
    df['title'] = df['title'].str.replace(char, " ")

print(f'Contents of the title column after cleaning:\n{df["title"]}')

# Remove two spaces
df['title'] = df['title'].str.split().str.join(" ")
print(f'Contents of the title column after cleaning:\n{df["title"]}')
print('**********************************************************************')
print(f'Title of Row 0:{df.loc[0].title}')
print(f'Title of Row 1:{df.loc[1].title}')
# print(spec_chars)
