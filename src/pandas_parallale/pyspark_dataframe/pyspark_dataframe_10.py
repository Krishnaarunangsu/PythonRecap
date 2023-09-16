import os
import sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, array_contains
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

data = [
        (('James', '', 'Smith'), ["Java","Scala", "C++"], "OH", 'M'),
        (('Anna', 'Rose', ''), ["Spark","Java", "C++"], "NY", 'F'),
        (('Julia', '', 'Williams'), ["CSharp","VB"], "OH", 'F'),
        (('Maria', 'Anne', 'Jones'), ["CSharp","VB"], "NY", 'M'),
        (('Jen', 'Mary', 'Brown'), ["CSharp","VB"], "NY", 'M'),
        (('Mike', 'Mary', 'Williams'), ["Python","VB"], "OH", 'M'),

        ]

columns = StructType([

        StructField('name', StructType([
                StructField('firstname', StringType(),True),
                StructField('middlename', StringType(),True),
                StructField('lastname', StringType(),True),
        ])),
        StructField('languages', ArrayType(StringType()),True),
        StructField('state', StringType(),True),
        StructField('gender',StringType(),True),

])

df = spark.createDataFrame(data=data, schema=columns)
df.printSchema()
print('*********************The Complete Dataframe***************')
df.show()

print('*********************The Filtered Dataframe***************')
# Filter on column using the equals condition
df.filter(df.state=='OH').show(truncate=False)

print('*********************The Filtered Dataframe***************')
# Filter on column using the equals condition
df.filter(df.state!='OH').show(truncate=False)

print('*********************The Filtered Dataframe***************')
# Filter on column using the equals condition
df.filter(~(df.state=='OH')).show(truncate=False)

print('*********************The Filtered Dataframe***************')
# Filter on column using the col() function
df.filter(col('state')=='OH').show(truncate=False)

print('*********************The Filtered Dataframe***************')
# Filter on column using the SQL expression
df.filter("gender =='M'").show()

# For not equal
print('*********************The Filtered Dataframe***************')
# Filter on column using the SQL expression
df.filter("gender !='M'").show()
print('*********************The Filtered Dataframe***************')
# Filter on column using the SQL expression
df.filter("gender <>'M'").show()

print('*********************The Filtered Dataframe***************')
# Filter with multiple conditions
df.filter((df.state=='OH') & (df.gender=='M')).show(truncate=False)

print('*********************The Filtered Dataframe***************')
# Filter IS IN LIST Values
state_list=["OH", "CA", "DE"]
df.filter(df.state.isin(state_list)).show()

print('*********************The Filtered Dataframe***************')
# Filter Not IS IN LIST Values
state_list=["OH", "CA", "DE"]
df.filter(~(df.state.isin(state_list))).show()

print('*********************The Filtered Dataframe***************')
# using startswith
df.filter(df.state.startswith('N')).show()

print('*********************The Filtered Dataframe***************')
# using endswith
df.filter(df.state.endswith('H')).show()


print('*********************The Filtered Dataframe***************')
# using endswith
df.filter(df.state.contains('H')).show()

print('*********************The Filtered Dataframe***************')
# Filtering an Array Column
df.filter(array_contains(df.languages, "JAVA")).show(truncate=False)
df.filter(array_contains(df.languages, "Java")).show(truncate=False)

print('*********************The Filtered Dataframe***************')
# Filtering an Nested Struct columns
df.filter(df.name.lastname=="Williams").show(truncate=False)


#Reference
# https://sparkbyexamples.com/pyspark/pyspark-where-filter/


