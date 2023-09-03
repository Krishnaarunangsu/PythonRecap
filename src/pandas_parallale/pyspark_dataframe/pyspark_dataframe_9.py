import os
import sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

data = [('James', '', 'Smith', '1991-04-01', 'M', 3000),
        ('Michael', 'Rose', '', '2000-05-19', 'M', 4000),
        ('Robert', '', 'Williams', '1978-09-05', 'M', 4000),
        ('Maria', 'Anne', 'Jones', '1967-12-01', 'F', 4000),
        ('Jen', 'Mary', 'Brown', '1980-02-17', 'F', -1)
        ]

columns = ["firstname", "middlename", "lastname", "dob", "gender", "salary"]
df = spark.createDataFrame(data=data, schema=columns)
df.printSchema()
df.show()

df_2=df.withColumn("salary", col("salary").cast("Integer"))
df_2.printSchema()
df_2.show()
print('**************************************************')

# Update The Value of an Existing Column
df_3=df.withColumn("salary",col("salary")*100)
print('Updated the values of an existing column')
df_3.show()

# Create a Column from an Existing
df_4=df.withColumn("CopiedColumn",col("salary")* -1)
print('Created a new column from an existing column')
df_4.show()
print('**************************************************')

# Add a New Column using withColumn()

# df_5=df_4.withColumn("Country", lit("USA"))
df_5=df_4.withColumn("Country", lit("USA")) \
  .withColumn("anotherColumn",lit("anotherValue"))
print('Two New Columns added')
df_5.show()
print('**************************************************')

# Rename Column Name
df_6=df_5.withColumnRenamed("gender","sex")
print('gender column is renamed to sex')
df_6.show()
print('**************************************************')

# Drop Column From PySpark DataFrame
df_7=df_6.drop("salary")
print('Salary Column is dropped')
df_7.show()