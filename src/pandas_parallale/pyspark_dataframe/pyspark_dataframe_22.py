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

list_1=[
    ('x', 5, 3, 7),
    ('Y', 3, 3, 6),
    ('Z', 5, 2, 6)
]
schema=['A', 'B', 'C', 'D']

df=None
try:
    df = spark.createDataFrame(list_1,schema)
except ValueError as ve:
    print(f'Some issue with value:{list_1}')
# print the dataframe
if df is not  None:
    df.show()
    print('***************************Print Schema****************************')
    df.printSchema()

# create the new column as by withcolumn
# by giving argument  as
# col_name ='expression_method_sum'
# and  expr() function which
# will take expressions  argument as string
df_col1 = df.withColumn('expression_method_sum',
                             expr("B+C+D"))
df_col1.show()
df_col1.printSchema()

df_col2 = df.withColumn('expression_method_product',
                             expr("B*C"))
df_col2.show()
df_col2.printSchema()




