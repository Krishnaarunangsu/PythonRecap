import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

# Spark Context textFile function reads a file and returns a RDD
# RDD-1
baby_names=spark.sparkContext.textFile('..//..//..//..//data//csv//baby_names_reduced.csv')
print(f'RDD to List:\n{baby_names.collect()}')
print('*********************************************************************')

# map
# Map transformation returns a new RDD by applying a function to each element of this RDD
# RDD-2
#rows = baby_names.map(lambda line: line.split(" "))
#rows = baby_names.map(lambda line: line.split(""))
# rows = baby_names.map(lambda line: line.split(","))
#crows = baby_names.map(lambda line: line.split(" ,"))
# for row in rows.take(rows.count()): print(row[1])
rows = baby_names.map(lambda line: line.split(","))
namesToCounties = rows.map(lambda n: (str(n[1]),str(n[2]) )).groupByKey()
data_col_1=namesToCounties.collect()
print(data_col_1)
print(namesToCounties.map(lambda x : {x[0]: tuple(x[1])}).collect())
print(namesToCounties.map(lambda x : {x[0]: set(x[1])}).collect())
print(namesToCounties.map(lambda x : {x[0]: list(x[1])}).collect())