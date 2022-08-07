# Read csv file
import pandas as pd

# path of the CSV file
csv_path = "..\\..\\..\\data\\csv\\Salaries.csv"

# Load the csv file and create the dataframe
df_csv = pd.read_csv(filepath_or_buffer=csv_path)
print(f'Salaries CSV to pandas Dataframe:\n{df_csv}')

