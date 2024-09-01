import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()
rdd_1=spark.sparkContext.textFile("C://Arunangsu//PythonRecap//data//data.txt")

# for element in rdd_1.collect():
    # print(element)

# flatMap() Transformation
rdd_2=rdd_1.flatMap(lambda x: x.split(" "))
print(rdd_2.collect())
for element in rdd_2.collect():
     print(element)