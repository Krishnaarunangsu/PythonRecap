import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

# Spark Context textFile function reads a file and returns a RDD
baby_names=spark.sparkContext.textFile('..//..//data//csv//baby_names_reduced.csv')
# print(baby_names)

# map
# Map transformation returns a new RDD by applying a function to each element of this RDD
rows = baby_names.map(lambda line: line.split(","))
data_col=rows.collect()
for row in data_col:
     print(row)
# for row in rows:
#     print(row)
#for row in rows.take(rows.count()): print(row[1])

# for element in rdd_1.collect():
    # print(element)

# flatMap() Transformation
# rdd_2=rdd_1.flatMap(lambda x: x.split(" "))
# #print(rdd_2)
# for element in rdd_2.collect():
#     print(element)