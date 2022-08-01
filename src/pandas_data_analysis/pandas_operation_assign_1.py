# Applying lambda function to single column using Dataframe.assign()
import pandas as pd

# Creating and initialising a list
values = [
    ['Rohan', 455],
    ['Elvish', 250],
    ['Deepak', 495],
    ['Soni', 400],
    ['Radhika', 350],
    ['Vansh', 450]
]

columns = ['Name', 'Total_Marks']

df = pd.DataFrame(values, columns=columns)

print(f'Original Dataframe:\n{df}')

# Applying lambda function to find percentage of 'Total_Marks' column using df.assign()
# Have a new calculated column "Percentage" calculated from the "Total_Marks" column
df = df.assign(Percentage=lambda x: (x['Total_Marks'] / 500 * 100))
print(f'Modified Dataframe:\n{df}')
