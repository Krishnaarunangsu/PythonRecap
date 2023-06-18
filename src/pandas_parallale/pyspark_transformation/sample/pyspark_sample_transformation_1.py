# import the pyspark module
import os
import sys

import pyspark

# import SparkSession for creating a session

from pyspark.sql import SparkSession

# import RDD from pyspark.rdd

from pyspark.rdd import RDD

# create an app named linuxhint
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark_app = SparkSession.builder.appName('linuxhint').getOrCreate()

# RDD-1
parallel = spark_app.sparkContext.parallelize(range(1,10))
count_1=parallel.sample(True,.2).count()
print(count_1)
count_2=parallel.sample(True,.2).count()
print(count_2)
count_3=parallel.sample(True,.2).count()
print(count_3)