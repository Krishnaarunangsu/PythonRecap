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

# RDD-2
filtered_rows = baby_names.filter(lambda line: "Count" not in line).map(lambda line: line.split(","))
print(f'Only the Data: {filtered_rows.collect()}')

# RDD-3
name_count=filtered_rows.map(lambda n:  (str(n[1]), int(n[4]) ) ).aggregateByKey(0, lambda k,v: int(v)+k, lambda v,k: k+v).collect()
print(f'Name-wise count over the years:{name_count}')