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

#rows = baby_names.map(lambda line: line.split(" "))
#rows = baby_names.map(lambda line: line.split(""))
rows = baby_names.map(lambda line: line.split(","))
rdd_6=rows.filter(lambda line: "MICHAEL" in line).collect()
print(f'RDD-6:{rdd_6}')

print(f'Coming Here')
for row_1 in rdd_6:
     print(f'Coming Here')
     print(row_1)
