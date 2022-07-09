# Example #1: Use bfill() function to populate missing values na values in the dataframe across rows.
import pandas as pd

# Creating a dataframe with "na" values.
df = pd.DataFrame({"A": [None, 1, 2, 3, None, None],
                   "B": [11, 5, None, None, None, 8],
                   "C": [None, 5, 10, 11, None, 8]})

print(f'Original Dataframe:\n{df}')

# When axis='rows', then value in current na cells are filled from the corresponding value in the next row.
# If the next row is also na value then it won’t be populated.
# Fill across the row
df.bfill(axis ='rows', inplace=True)
print(f'Modified Dataframe:\n{df}')
