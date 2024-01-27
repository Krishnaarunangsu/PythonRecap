import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

# range: creates a new RDD ranging from 0 to n-1
# collect: returns a list that contains all the elements of this RDD
data_collect_1=spark.sparkContext.range(5).collect()
print(f'Elements of the RDD:{data_collect_1}')