import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

rdd_1=spark.sparkContext.parallelize([1, 2, 3])
rdd_2=rdd_1.flatMap(lambda x: [x,x,x])
dataset=rdd_2.collect()
dataset_count=rdd_2.count()
print(f'The dataset is:{dataset}')
print(f'The dataset count is:{dataset_count}')

