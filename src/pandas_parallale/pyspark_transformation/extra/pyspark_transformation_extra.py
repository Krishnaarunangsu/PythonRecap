# You cannot use flatMap on an Int object
# flatMap can be used in collection objects such as Arrays or list.
# You can use map function on the rdd type that you have RDD[Integer]
import os
import sys
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()
numbersRDD = spark.sparkContext.parallelize([1, 2, 3, 4])
actionRDD = numbersRDD.map(lambda x: x + x)

def printing(x):
    print(x)

actionRDD.foreach(printing)