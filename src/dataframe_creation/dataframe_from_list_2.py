# Create Dataframe from Lists
# Import pandas library
import pandas as pd

# initialize list elements
data_1 = [10, 20, 30, 40, 50, 60]
data_2 = [11, 21, 31, 41, 51, 61]
data_3 = [12, 22, 32, 42, 52, 62]
data= zip(data_1, data_2, data_3)

# Create the pandas DataFrame with column name is provided explicitly
df = pd.DataFrame(data, columns=['Numbers_1', 'Numbers_2','Numbers_3'])

# print dataframe.
print(f'The Dataframe from the list is:\n{df}')
