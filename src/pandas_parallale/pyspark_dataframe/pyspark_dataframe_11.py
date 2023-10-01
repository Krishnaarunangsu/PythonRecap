import os
import sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, array_contains
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()


data2 = [(2,"Michael Rose"),(3,"Robert Williams"),
     (4,"Rames Rose"),(5,"Rames rose")
  ]
df2 = spark.createDataFrame(data = data2, schema = ["id","name"])

# PySpark Filter like and rlike
# like - SQL LIKE pattern
df2.filter(df2.name.like("%rose%")).show()


# rlike - SQL RLIKE pattern (LIKE with Regex)
#This check case-insensitive
df2.filter(df2.name.rlike("(?i)^*rose$")).show()

