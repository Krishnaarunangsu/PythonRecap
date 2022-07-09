import pandas as pd

df = pd.DataFrame({
    'Pokeman': ['Bulbasur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon'],
    'Type': ['Grass', 'Grass', 'Grass', 'Fire', 'Fire']
})

print(f'Original Dataframe:\n{df}')

# Insert a column with default values
df.insert(loc=2, column="Team", value="Any")
print(f'Modified Dataframe:\n{df}')

# creating a blank series
Type_new = pd.Series([])
# Passing series with different value for each row:
for i in range(len(df)):
    if df["Type"][i] == "Grass":
        Type_new[i] = "Green"

    elif df["Type"][i] == "Fire":
        Type_new[i] = "Orange"

    elif df["Type"][i] == "Water":
        Type_new[i] = "Blue"

    else:
        Type_new[i] = df["Type"][i]

# inserting new column with values of list made above
df.insert(2, "Type New", Type_new)

print(f'Modified Dataframe:\n{df}')

# drop the previously added column
df.drop(columns="Team", axis=1, inplace=True)

print(f'Modified Dataframe:\n{df}')
