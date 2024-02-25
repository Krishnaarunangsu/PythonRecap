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

# Create Dataframe from list of tuples
list_1=[
    ('x', 5, 3, 7),
    ('Y', 3, 3, 6),
    ('Z', 5, 2, 6)
]

# Dataframe Columns
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

# select everything from table df_col1 and
# create new sum  column as " select_method_sum".
df_col1 = df.select('*',
                         (df["B"]+df["C"]+df['D']).alias("select_method_sum"))
df_col1.show()
df_col1.printSchema()




