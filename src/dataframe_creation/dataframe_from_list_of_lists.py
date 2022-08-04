#  Creating Pandas DataFrame from lists of lists.
# Import pandas library
import pandas as pd

# initialize list of lists
data = [
           ['tom', 10],
           ['nick', 15],
           ['juli', 14]
      ]

columns = ['Name', 'Age']

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=columns)

# print dataframe.
print(f'The Dataframe from the List of Lists is:\n{df}')
