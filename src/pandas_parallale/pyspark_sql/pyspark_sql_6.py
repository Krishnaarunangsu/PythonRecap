import os
import sys
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
# import findspark

# findspark.init()

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Create a spark session for DataFrame and SQL work
spark=SparkSession.builder.master("local").appName(" Spark SQL Example").getOrCreate()
df=spark.sql("select 'spark' as hello")
df.show()

