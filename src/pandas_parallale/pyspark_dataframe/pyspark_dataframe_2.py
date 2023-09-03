import os
import sys
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.getOrCreate()
# df = spark.createDataFrame([
#     Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
#     Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
#     Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
# ])

data=[("Alice", 1),("Bob", 2),("Charlie", 3)]
df=spark.createDataFrame(data,["name", "age"])
print(df.head())
print(df.show())

# Select only the "name" column from the PySpark Dataframe
print(df.select('name').show())

# Filter the rows based on a condition
print(df.filter(df.age>1).show())

# Group the data by the "age" column and compute the average "age"
print(df.groupBy('age').avg().show())

feature_group = ['name', 'age']
data_counts = df.groupBy(feature_group).count().alias("counts")
data_joined = df.join(data_counts, feature_group)
print(data_joined.show())

feature_group = ['name', 'age']
data_avg = df.groupBy('name','age').avg().alias("average_age")
data_joined_avg = df.join(data_avg, feature_group)
print(data_joined_avg.show())
