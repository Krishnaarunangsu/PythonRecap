import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

# Spark Context textFile function reads a file and returns a RDD
# RDD-1

rdd_1=spark.sparkContext.parallelize([('a', 1), ('b', 1), ('c', 1)])