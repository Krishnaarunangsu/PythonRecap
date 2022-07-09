# Example #2: Use bfill() function to populate missing values na values in the dataframe across columns.
import pandas as pd

df = pd.DataFrame({"A": [None, 1, 2, 3, None, None],
                   "B": [11, 5, None, None, None, 8],
                   "C": [None, 5, 10, 11, None, 8]})

print(f'Original Dataframe:\n{df}')

# when axis='columns', then the current na cells will be filled from the value present in the next column in the same
# row. If the next column is also na cell then it won’t be filled.
# bfill values using values from next column
df.bfill(axis='columns', inplace=True)
print(f'Modified Dataframe:\n{df}')
