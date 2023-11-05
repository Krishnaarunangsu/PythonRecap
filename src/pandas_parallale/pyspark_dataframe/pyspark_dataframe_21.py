# Create PySpark DataFrame from an inventory of rows
import os
import sys
from datetime import datetime, date
from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import col, lit, array_contains
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

list_1=[
    Row(a=1, b=4., c='GFG1', d=date(2000, 8, 1),
     e=datetime(2000, 8, 1, 12, 0)),

    Row(a=2, b=8., c='GFG2', d=date(2000, 6, 2),
     e=datetime(2000, 6, 2, 12, 0)),

    Row(a=3, b=5., c='GFG3', d=date(2000, 5, 3),
     e=datetime(2000, 5, 3, 12, 0))
]

df=None
try:
    df = spark.createDataFrame(list_1)
except ValueError as ve:
    print(f'Some issue with value:{list_1}')
# print the dataframe
if df is not  None:
    df.show()
    print('***************************Print Schema****************************')
    df.printSchema()

# show schema




