import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit,when

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Create a spark session for DataFrame and SQL work
spark=SparkSession.builder.master("local").appName(" Spark SQL Example").getOrCreate()

# Create a DataFrame
dataset=[("Alice",25),("Bob", 30), ("Charlie", 35)]
columns=["Name","Age"]
df=spark.createDataFrame(dataset,schema=columns)


# Adding a new column
df = df.withColumn('Gender', lit('Female'))
# Print the Dataframe
df.show()
# df=df.withColumn('Gender', when(df.Name=='Bob', 'Male')) # This will prouce null for non-matching rows
df=df.withColumn('Gender', when(df.Name=='Bob', 'Male').otherwise(df.Gender))
df.show()