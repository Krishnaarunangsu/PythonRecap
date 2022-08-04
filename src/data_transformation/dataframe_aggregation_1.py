# Aggregate ‘sum’ and ‘min’ function across all the columns in data frame.
import pandas as pd

# Making Dataframe from CSV file
df_nba = pd.read_csv("..\\..\\data\\csv\\nba.csv")
print(f'NBA Dataframe-5 rows:\n{df_nba.head(n=5)}')
print(f'***************************************************')
# Dataframe columns
df_columns = df_nba.columns.tolist()
print(f'NBA Dataframe Columns:{df_columns}')
print(f'***************************************************')

# Dataframe Numeric columns
df_nba_numerical_cols = df_nba.select_dtypes(include='number').columns.tolist()
print(f'NBA Dataframe Numerical Columns:{df_nba_numerical_cols}')
print(f'***************************************************')

# Aggregation works with only numeric type columns. Applying aggregation across all the columns
# sum and min will be found for each numeric type column in df dataframe
# Column Data Types: Get numerical Datatypes only
column_types = df_nba.select_dtypes(include='number').dtypes
print(f'NBA Dataframe Column-Types:\n{column_types}')
print(f'***************************************************')

# Aggregate on the Numeric Columns
df_column_sum_min = (df_nba.select_dtypes(include='number')).aggregate(['sum', 'min'])
print(f'Dataframe after aggregation:\n{df_column_sum_min}')
