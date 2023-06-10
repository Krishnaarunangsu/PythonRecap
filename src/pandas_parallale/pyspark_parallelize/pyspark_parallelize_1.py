import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
# Creates a Spark Session
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

list_data_1=([1, 2, 3, 4, 5, 6])

# Convert the list into RDD
# rdd_1=spark.sparkContext.parallelize(list_data_1, 4)
rdd_1=spark.sparkContext.parallelize(list_data_1)
print(f'Type of rdd_1:{type(rdd_1)}')
print(f' Number of partitions:{rdd_1.getNumPartitions()}')
print(f'RDD Empty check:{rdd_1.isEmpty()}')
