import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

rdd_1=spark.sparkContext.parallelize(['abbe', 'abby', 'apple'])
dataset=rdd_1.collect()
dataset_count=rdd_1.count()
print(f'The dataset is:{dataset}')
print(f'The dataset count is:{dataset_count}')

