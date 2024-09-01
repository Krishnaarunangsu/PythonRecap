import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()
# rdd_1=spark.sparkContext.textFile('data.txt')

# for element in rdd_1.collect():
# print(element)
data = ["Project Gutenberg’s",
        "Alice’s Adventures in Wonderland",
        "Project Gutenberg’s",
        "Adventures in Wonderland",
        "Project Gutenberg’s"]
rdd = spark.sparkContext.parallelize(data)
for element in rdd.collect():
    print(element)
# flatMap() Transformation
rdd_2 = rdd.flatMap(lambda x: x.split(" "))
print(rdd_2)
for element in rdd_2.collect():
    print(element)
