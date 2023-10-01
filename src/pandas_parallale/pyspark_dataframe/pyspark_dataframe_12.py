# pyspark.sql.DataFrame.withColumn
# DataFrame.withColumn(colName: str, col: pyspark.sql.column.Column)
# Returns a new DataFrame by adding a column or replacing the existing column that has the same name.
# The column expression must be an expression over this DataFrame; attempting to add a column from some other DataFrame will raise an error.

import os
import sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, array_contains
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

# Create the dataframe
df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
# Add a column based on an existing column
df.withColumn('age2', df.age + 2).show()


# In a more performance-optimized way
df.select(df.name, (df.age + 10).alias('age')).show()
df_2=df.select(df.name, df.age.alias('agemeasure'))
print(df_2.show())
df.select(df.name,df.age, (df.age + 10).alias('age2')).show()


