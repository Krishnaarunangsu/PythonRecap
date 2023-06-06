import pyspark
from pyspark.sql import SparkSession
import os,sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark=SparkSession.builder.appName("PySpark_Parallel").getOrCreate()
sparkContext=spark.sparkContext

# Now, use sparkContext.parallelize() to create rdd from a list or collection.
rdd=sparkContext.parallelize([1,2,3,4,5])
#print(rdd)
print(f'Number of Partitions:{rdd.getNumPartitions()}')
print(f'The first element:{rdd.first()}')
rddCollect=rdd.collect()
print(f'The Collections from the nodes:{rddCollect}')
print(rdd.max())
print(rdd.min())
