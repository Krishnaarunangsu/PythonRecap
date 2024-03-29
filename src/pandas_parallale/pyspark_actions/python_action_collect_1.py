import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

rdd_1=spark.sparkContext.parallelize([1, 2, 3])
print(f'RDD_1:{rdd_1.collect()}')
rdd_2=rdd_1.flatMap(lambda x: [x,x,x])
dataset=rdd_2.collect()
print(f'RDD_2:-The dataset is:{dataset}')
