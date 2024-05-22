# Add column sum as new column in PySpark dataframe
import os
import sys
from datetime import datetime, date
from pyspark.sql import SparkSession, Row
# import expr from the functions
from pyspark.sql.functions import expr
from pyspark.sql.functions import col, lit, array_contains
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('sum as new_col').getOrCreate()

# df = spark.createDataFrame([
#     Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
#     Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
#     Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
# ])
schema = StructType([
        StructField('name', StructType([
             StructField('firstname', StringType(), True),
             StructField('middlename', StringType(), True),
             StructField('lastname', StringType(), True)
             ])),
         StructField('dob', StringType(), True),
         StructField('gender', StringType(), True),
         StructField('salary', IntegerType(), True)
         ])
data_df=[
    (('James','','Smith'),'1991-04-01','M', 3000),
(('Michael','Rose',''),'2000-05-19','M', 4000),
(('Robert','','William'),'1978-09-05','M', 4000),
(('Maria','Anne','Jones'),'1967-12-01','F', 4000),
(('Jen','Mary','Brown'),'1980-17-02','F', -1)

]
df=spark.createDataFrame(data=data_df, schema=schema)
df.printSchema()
df.head()
df.show()
print('***********************************************')
# Rename the dob column to DateOfBirth
df2=df.withColumnRenamed('dob','DateOfBirth')
df2.printSchema()
df2.show()

df.withColumnRenamed("gender","Gender") \
    .withColumnRenamed("salary","Salary").printSchema()

# Using PySpark StructType – To rename a nested column in Dataframe
schema2=StructType([
    StructField('fname', StringType()),
    StructField('middlename', StringType()),
    StructField('lname', StringType())
])

df.select(col('name').cast(schema2),
          col("dob"), col("gender"),
          col("salary")).printSchema()

# Using Select – To rename nested elements.
df.select(col('name.firstname').alias('fname'),
          col('name.middlename').alias('mname'),
          col('name.lastname').alias('lname')
          ).printSchema()

df4=df.withColumn("fname",col("name.firstname"))\
    .withColumn("mname",col("name.middlename"))\
    .withColumn("lname",col("name.lastname")).drop("name")
# df4.drop("name")
df4.printSchema()
df4.show()
