from pyspark.sql import SparkSession
import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

print(spark)
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
print(f'RDD Count:{rdd.count()}')
