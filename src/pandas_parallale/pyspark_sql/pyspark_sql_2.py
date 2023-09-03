import sys
import os
from pyspark.sql import Row, SparkSession
from pyspark.sql.functions import col

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('SparkExample_1').getOrCreate()

# Read CSV file  into a Session-Scoped Temporary Table
spark.read.option("header", True) \
      .csv("sample_zipcodes.csv") \
      .createOrReplaceTempView('Zipcodes')
print('The Session-Scoped Temporary Table is')
# Run the sql-query
spark.sql("select * from Zipcodes").show()
