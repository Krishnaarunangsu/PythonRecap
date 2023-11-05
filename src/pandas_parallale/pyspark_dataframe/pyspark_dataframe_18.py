# Create Pyspark Dataframe from pandas dataframe
import os
import sys
from datetime import datetime, date

import pandas as pd
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, array_contains
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

data={
    'a':[1, 2, 3],
    'b':[4.,8.,5.],
    'c':['GFG1', 'GFG2','GFG3'],
    'd':[date(2000, 8, 1), date(2000, 6, 2),
          date(2000, 5, 3)],
    'e': [datetime(2000, 8, 1, 12, 0),
          datetime(2000, 6, 2, 12, 0),
          datetime(2000, 5, 3, 12, 0)]
}
pandas_df=pd.DataFrame(data)
print(pandas_df)
df=None
try:
    df = spark.createDataFrame(pandas_df)
except ValueError as ve:
    print(f'Some issue with value:{data}')
# print the dataframe
if df is not  None:
    df.show()
    print('***************************Print Schema****************************')
    df.printSchema()

# show schema




