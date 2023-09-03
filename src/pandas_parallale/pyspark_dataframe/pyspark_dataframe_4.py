import os
import sys
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row, SparkSession
from pyspark.sql.functions import col

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkExample_1').getOrCreate()
# df = spark.createDataFrame([
#     Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
#     Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
#     Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
# ])

data=[
    ("James", 'Smith','USA','CA'),
    ("Michael", 'Rose','USA','NY'),
    ("Robert", 'Williams','USA','CA'),
    ("Maria", 'Jones','USA','FL'),
    ]
columns=["firstname", "lastname","country", "state"]
df=spark.createDataFrame(data,schema=columns)
print(df.head())
print(df.show(truncate=False))

# Select All columns from List
print(df.select(*columns).show())

# Select All columns from List
print(df.select([col for col in df.columns]).show())
print(df.select("*").show())



# feature_group = ['name', 'age']
# data_avg = df.groupBy('name','age').avg().alias("average_age")
# data_joined_avg = df.join(data_avg, feature_group)
# print(data_joined_avg.show())
