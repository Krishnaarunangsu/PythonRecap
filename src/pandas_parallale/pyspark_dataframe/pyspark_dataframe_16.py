# Create Pyspark Dataframe from Text
import os
import sys
import pandas as pd
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, array_contains
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

path="C://Arunangsu/PythonRecap/data/txt/data_1.txt"

# Create the dataframe from JSON
df = spark.createDataFrame(pd.read_csv(path, delimiter="\t"))
# print the dataframe
df.show()
print('***************************Print Schema****************************')
# show schema
df.printSchema()



