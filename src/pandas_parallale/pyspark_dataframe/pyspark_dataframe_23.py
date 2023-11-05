# Add column sum as new column in PySpark dataframe
import os
import sys
from datetime import datetime, date
from pyspark.sql import SparkSession, Row
# import expr from the functions
from pyspark.sql.functions import expr
import pyspark.sql.functions as F
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


# define the sum_col
def sum_col(b, c, d):
    col_sum = b + c + d
    return col_sum


# integer datatype is defined
new_f = F.udf(sum_col, IntegerType())

# calling and creating the new
# col as udf_method_sum
df_col1 = df.withColumn("Udf_method_sum",
                          new_f("B", "C", "D"))
df_col1.show()
df_col1.printSchema()






