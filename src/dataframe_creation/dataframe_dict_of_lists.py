# Python code demonstrate creating DataFrame from dict ndarray / lists By default addresses

# Import the library
import pandas as pd

# initialize data of lists.
data = {
    'Name': ['Tom', 'nick', 'krish', 'jack'],
    'Age': [20, 21, 19, 18]
}

# Create the Dataframe
# Note: While creating dataframe using dictionary, the keys of dictionary will be column name by default.
# We can also provide column name explicitly using column parameter.
profile_dataframe = pd.DataFrame(data=data)
print(profile_dataframe)
