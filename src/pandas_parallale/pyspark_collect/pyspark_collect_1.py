import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
# Creates a Spark Session
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()



