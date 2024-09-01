import sys
import os
from pyspark.sql import Row, SparkSession

import pandas as pd

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
# Create a SparkSession
spark = SparkSession.builder.appName("Map\
TransformationExample").getOrCreate()

# Read in a dataset
df = spark.read.csv("C://Arunangsu//PythonRecap//data//csv//data.csv",
                    header=True)


# Use map() to apply a function
# to each row of the dataframe
def extract_features(row):
    return (float(row.feature1),
            float(row.feature2))


rdd = df.rdd.map(extract_features)


# Use the map() transformation to apply
# a function to each element of the rdd
def normalize(row):
    try:
        return (row[0] / 10, row[1] / 100)
    except TypeError:
        # Return a default value if the
        # input values are not numeric
        return (0, 0)


rdd_normalized = rdd.map(normalize)

# Use the collect() action to retrieve
# the transformed elements of the rdd
normalized_data = rdd_normalized.collect()

# print transform data
for row in normalized_data:
    print(row)

# Stop the SparkSession
spark.stop()

