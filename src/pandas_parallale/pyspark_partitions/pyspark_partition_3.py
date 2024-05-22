import pyspark, os, sys
from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('answer').getOrCreate()

# rdd=spark.sparkContext.parallelize(range(0,20))
rdd=spark.sparkContext.parallelize((0,20))
print(f'From local[5]:{str(rdd.getNumPartitions())}')

rdd=spark.sparkContext.parallelize((0,25),8)
print(f'From local[5]:{str(rdd.getNumPartitions())}')

rdd_data=rdd.collect()
print(rdd_data)

rdd_from_file=spark.sparkContext.textFile("test.txt")
print(f'TextFile:{str(rdd_from_file.getNumPartitions())}')

rdd1=spark.sparkContext.parallelize(range(0,20),6)
rdd1.saveAsTextFile("test1.txt")
