from pyspark import SparkContext
import os
import sys

big_list=range(100)

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

sc = SparkContext("local", "Big_Data App")
print('************************************RDD-1***************************************')
# rdd = sc.parallelize(big_list,2)
rdd = sc.parallelize(big_list)
print(f'Count in RDD:{rdd.count()}')
print(f'Number of Partitions:{rdd.getNumPartitions()}')
print('************************************RDD-2***************************************')
odds = rdd.filter(lambda num: num % 2 != 0)
print(f'First 20 odd numbers:\n{odds.take(20)}')