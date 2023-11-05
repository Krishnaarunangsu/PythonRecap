import os
import sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, array_contains
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

data=[('James', 'Smith', 'M', 3000), ('Anna', 'Rose', 'F', 4100),('Robert', 'Williams','M',6200)]
# data=[('James', 'Smith'), ('Anna', 'Rose'),('Robert', 'Williams')]
# columns=["firstname","lastname"]
columns=["firstname","lastname","gender","salary"]

# Create the dataframe
df = spark.createDataFrame(data=data, schema=columns)
# print the dataframe
df.show()
print('***************************Add a Constant Column****************************')
# Add a New Constant Column witj lit()
df_2=df.withColumn("bonus_percent", lit(0.3))
# print the dataframe
df_2.show()
# df.select(*columns,lit(0.3).alias("bonus_percent1")).show()
# df.select(*columns).show()
df_2.select(*columns).show()
df_2.select('*').show()


