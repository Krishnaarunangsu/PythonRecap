import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial Group By Key').getOrCreate()

# Spark Context textFile function reads a file and returns a RDD
# RDD-1

rdd_1=spark.sparkContext.parallelize([("Apple",1),("Banana",1),("Apple",1),("Apple",1),("Orange",1),("Orange",1)])
rdd_group_key_count=rdd_1.groupByKey().mapValues(len).collect()
print(f'Group Key Count:{rdd_group_key_count}')

rdd_group_key_items=rdd_1.groupByKey().mapValues(list).collect()
print(f'Group Key Items:{rdd_group_key_items}')

# https://proedu.co/spark/apache-spark-rdd-groupbykey-transformation/
# https://www.javatpoint.com/apache-spark-groupbykey-function
# https://medium.com/@sujathamudadla1213/explain-the-difference-between-groupbykey-and-reducebykey-bf0171e985ac