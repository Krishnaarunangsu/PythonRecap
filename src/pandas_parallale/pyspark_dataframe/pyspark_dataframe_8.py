import os
import sys
from datetime import datetime, date
from pyspark.sql import Row, SparkSession
from pyspark.sql.functions import col, lit

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('Jagannath').getOrCreate()


data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

df = spark.createDataFrame(data=data, schema = columns)
print(df.dtypes)
print(df.describe())
df.show()

# Change DataType using PySpark withColumn()
df.withColumn("salary", col("salary").cast("Integer")).show()
print(df.dtypes)
print(df.describe())

# Update The Value of an Existing Column
df.withColumn("salary",col("salary")*100).show()

# Create a Column from an Existing
df.withColumn("CopiedColumn",col("salary")* -1).show()

# Add a New Column using withColumn()

df.withColumn("Country", lit("USA")).show()
df.withColumn("Country", lit("USA")) \
  .withColumn("anotherColumn",lit("anotherValue")) \
  .show()

df.show()

# Rename Column Name
df.withColumnRenamed("gender","sex") \
  .show(truncate=False)

# Drop Column From PySpark DataFrame

df.drop("salary") \
  .show()


