import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()


# returns a new RDD by applying a function to each element of the RDD.
# Function in map can return only one item.

rdd = spark.sparkContext.parallelize(["b", "a", "c"])
print(rdd.map(lambda x: (x, 1)).collect())
print(sorted(rdd.map(lambda x: (x, 1)).collect()))

rdd_2 = spark.sparkContext.parallelize([1,2,3])
print(rdd_2.map(lambda x: (x, x*x)).collect())
print(sorted(rdd_2.map(lambda x: (x, 1)).collect()))
