import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()


#baby_names = spark.sparkContext.textFile('..//..//..//..//data//csv//baby_names.csv')
baby_names = spark.sparkContext.textFile('..//..//..//..//data//csv//baby_names_reduced.csv')
print(baby_names.collect())
print(baby_names.map(lambda x: x.split(",")).collect())
rows=baby_names.map(lambda x: x.split(",")).collect()
print(type(rows))

for row in rows:
    print(type(row))
    print(row[1])