import sys
import os
from pyspark.sql import Row, SparkSession
from pyspark.sql.functions import col

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('SparkExample_1').getOrCreate()

# Read CSV file into a Table
zipcode_df=spark.read.option("header",True) \
    .csv("sample_zipcodes.csv")
zipcode_df.printSchema()
print(zipcode_df.head(5))
zipcode_df.show()