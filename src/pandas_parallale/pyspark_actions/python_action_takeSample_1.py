import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

rdd_1=spark.sparkContext.parallelize(['twins', 'brewers', 'cubs', 'white sox','indians', 'bad news bears'])
dataset_first=rdd_1.takeSample(withReplacement=False,num=4)
print(f'The first three elements of the dataset are:{dataset_first}')


