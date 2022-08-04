# Creating DataFrame using zip() function.
# Two lists can be merged by using list(zip()) function.
# Now, create the pandas DataFrame by calling pd.DataFrame() function.

import pandas as pd

# List1
Name = ['tom', 'krish', 'nick', 'juli']

# List2
Age = [25, 30, 26, 22]

# get the list of tuples from two lists and merge them by using zip().
list_of_tuples = list(zip(Name, Age))

# Assign data to tuples.
print(f'List after zip:\n{list_of_tuples}')

# Converting lists of tuples into pandas Dataframe.
df = pd.DataFrame(list_of_tuples, index=['row_1', 'row_2'],
                  columns=['Name', 'Age'])

# Print data.
print(f'The Dataframe is:\n{df}')
