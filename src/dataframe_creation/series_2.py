import pandas as pd

# Create the Series
ser = pd.Series([20000, 25000, 23000, 28000, 55000, 23000, 28000])

# Create the Index
index = ['Java', 'Spark', 'PySpark', 'Pandas', 'NumPy', 'Python', "Oracle"]

# Set the index
ser.index = index
print(ser)


# Use iterate over index series
for indx in ser:
    print(indx)


# Iterate over all the elements using Series.iteritems()
for indx in ser.items():
    print(indx)


