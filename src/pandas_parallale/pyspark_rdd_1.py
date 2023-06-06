from pyspark import SparkContext
import os
import sys

big_list=range(100)

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

sc = SparkContext("local", "Big_Data App")
rdd = sc.parallelize(big_list,2)
odds = rdd.filter(lambda num: num % 2 != 0
                  )
print(odds.take(20))