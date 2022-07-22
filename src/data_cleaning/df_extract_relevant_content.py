import pandas as pd

df = pd.read_csv("..\\..\\data\\flights_tickets_serp2018-12-16.csv")

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

# Extract relevant content from a Series
# df['dollar_prices'] = df['title'].str.extract('(\$\.d*\.?\d*)')
df['dollar_prices'] = df['title'].str.extract('(\$\.d*\.?\d*)')
print(df['dollar_prices'])
