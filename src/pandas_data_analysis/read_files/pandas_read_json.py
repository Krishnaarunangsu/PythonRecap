# Load the JSON file into a DataFrame:
import pandas as pd

# Reads the json file and converts into a dataframe
df = pd.read_json("../../../data/json/data.json")

# use to_string() to print the entire DataFrame.
print(df.to_string())
