import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Create a spark session for DataFrame and SQL work
spark=SparkSession.builder.master("local").appName(" Spark SQL Example").getOrCreate()

# Create a DataFrame
dataset=[("Alice",25),("Bob", 30), ("Charlie", 35)]
columns=["name","Age"]
df=spark.createDataFrame(dataset,schema=columns)
# Print the Dataframe
df.show()


#Perform a Transformation
df_filtered=df.filter(df['Age']>30)

#Print the filtered dataframe
df_filtered.show()

df2=df.withColumn('age2', df.Age + 2)


# Adding a new column
df2 = df2.withColumn('Gender', lit('Female'))
df2.show()
