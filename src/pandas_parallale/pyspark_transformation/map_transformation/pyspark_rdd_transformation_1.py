import sys
import os
from pyspark.sql import Row, SparkSession

import pandas as pd

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

data=[1,2,3,4]
rdd=spark.sparkContext.parallelize(data)
rdd_transformed=rdd.map(lambda x:x*2)
print(f'Transformed RDD:{rdd_transformed.collect()}')