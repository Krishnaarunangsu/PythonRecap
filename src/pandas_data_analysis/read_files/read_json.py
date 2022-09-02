# Load the JSON file into a DataFrame:
import pandas as pd

json_file_path = "../../../data/json/data_1.json"
# Reads the json file and converts into a dataframe
df = pd.read_json(path_or_buf=json_file_path)

# use to_string() to print the entire DataFrame.
print(df.info)