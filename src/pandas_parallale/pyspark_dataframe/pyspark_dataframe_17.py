# Create Pyspark Dataframe from CSV
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

path="C://Arunangsu/PythonRecap/data/csv/train_dataset-1.csv"

# Create the dataframe from JSON
df = spark.createDataFrame(pd.read_csv(path))
# print the dataframe
df.show()
print('***************************Print Schema****************************')
# show schema
df.printSchema()



