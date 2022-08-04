import pandas as pd

# Data for the Marks
data = [
    [45, 52, 37, 61, 94, 99, 100],
    [87, 69, 95, 53, 90, 98, 80],
]

# row index
index = ['AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG']

# Columns
columns = ['Mathematics', 'Physics']

# Create Dataframe with index/row/label and columns(column names)
marks_dataframe = pd.DataFrame(data=data, index=index)
print(f'The marks dataframe is:\n{marks_dataframe}')
