import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

# Spark Context textFile function reads a file and returns a RDD
# RDD-1
baby_names=spark.sparkContext.textFile('..//..//data//csv//baby_names_reduced.csv')
print(f'RDD-1:\n{baby_names.collect()}')
print('*********************************************************************')

# map
# Map transformation returns a new RDD by applying a function to each element of this RDD
# RDD-2
#rows = baby_names.map(lambda line: line.split(" "))
#rows = baby_names.map(lambda line: line.split(""))
# rows = baby_names.map(lambda line: line.split(","))
rows = baby_names.map(lambda line: line.split(" ,"))
# for row in rows.take(rows.count()): print(row[1])
print(f'No of partitions:{rows.getNumPartitions()}')
print('**********************************************************************')
# List-1
data_col=rows.collect()
print(f'List from RDD-2:\n{data_col}')
print('**********************************************************************')
for idx, row in enumerate(data_col):
     # print(type(row))
     # print(type(row[0]))
     print('********************************List*******************************')
     print(type(data_col[idx]))
     print(data_col[idx])
     print(type(row))
     print(row)
     print('********************************String*******************************')
     print(type(row[0]))
     res: object=row[0]
     #print(type(res))
     print(row[0]) # String
     x=res.split(",") # List
     print('********************************After Splitting a String*******************************')
     print(type(x))
     print(x)
     #print(res.split(","))
     # List Comprehension
     print('--------------------------List Comprehension----------------')
     [print(y) for y in x]
     print("----------------------------FOR LOOP------------------------")
     for index, item in enumerate(x):
          # print(index, item)
           print(x[index])
     print('##########################################################################')
#     print(str(idx)+"-"+str(row[0]))
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