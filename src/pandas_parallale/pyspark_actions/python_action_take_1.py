import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

rdd_1=spark.sparkContext.parallelize(['abbe', 'abby', 'apple'])
dataset_first=rdd_1.take(2)
print(f'The first two elements of the dataset are:{dataset_first}')


