# Create PySpark DataFrame with an explicit schema
import os
import sys
from datetime import datetime, date

import pandas as pd
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, array_contains
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

data=[
    (1, 4., 'GFG1', date(2000, 8, 1),
     datetime(2000, 8, 1, 12, 0)),

    (2, 8., 'GFG2', date(2000, 6, 2),
     datetime(2000, 6, 2, 12, 0)),

    (3, 5., 'GFG3', date(2000, 5, 3),
     datetime(2000, 5, 3, 12, 0))
]
schema='a long, b double, c string, d date, e timestamp'

df=None
try:
    df = spark.createDataFrame(data,schema)
except ValueError as ve:
    print(f'Some issue with value:{data}')
# print the dataframe
if df is not  None:
    df.show()
    print('***************************Print Schema****************************')
    df.printSchema()

# show schema




