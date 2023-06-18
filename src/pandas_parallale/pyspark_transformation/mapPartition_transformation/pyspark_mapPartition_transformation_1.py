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


one_through_9 = range(1,10)
print(one_through_9)
parallel = spark_app.sparkContext.parallelize(one_through_9, 3)
def f(iterator):
    yield sum(iterator)
data_coll_1=parallel.mapPartitions(f).collect()
print(data_coll_1)

parallel = spark_app.sparkContext.parallelize(one_through_9)
data_coll_2=parallel.mapPartitions(f).collect()
print(data_coll_2)