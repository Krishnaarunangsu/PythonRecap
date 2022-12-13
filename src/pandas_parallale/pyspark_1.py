from pyspark.sql import SparkSession
import os
import sys

# https://stackoverflow.com/questions/68705417/pycharm-error-java-io-ioexception-cannot-run-program-python3-createprocess
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

print(spark)
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
print(f'RDD Count:{rdd.count()}')
print(f'The first Row:{rdd.take(1)}')

squared = rdd.map(lambda x: x*x).collect()
for num in squared:
    print('%i ' % (num))
