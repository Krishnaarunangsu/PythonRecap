# Select the Name from Row_2
import pandas as pd

json_Data={
    "Weight": [45, 88, 56, 15,71],
    "Name": ["Sam", "Andrea", "Alex", 'Robin', 'Kia'],
    "Age": [14, 25, 55, 8, 21]
}

# Create the DataFrame
df=pd.DataFrame(json_Data)
print(f'The Dataframe is:\n{df}')
print('********************************************')
print(f'The Default Index is:\n{df.index.values}')

# Create the index
index_= ["Row_1", "Row_2", "Row_3", "Row_4", "Row_5"]
# Update the index
df.index=index_
print(f'The Dataframe with the updated is:\n{df}')
print('********************************************')
print(f'The New Index is:\n{df.index.values}')

# Get the value of the name from the Row_2
result=df.loc["Row_2", "Name"]

# Display the result
print("\nSelected Value at Row_2, Column 'Name':")
print(result)
