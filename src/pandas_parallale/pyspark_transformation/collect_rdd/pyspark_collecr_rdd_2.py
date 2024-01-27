import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

# range: Distributes a local Python collection to form an RDD
# collect: returns a list that contains all the elements of this RDD
data_collect_1=spark.sparkContext.parallelize(["x", "y", "z"]).collect()
print(f'Elements of the RDD:{data_collect_1}')