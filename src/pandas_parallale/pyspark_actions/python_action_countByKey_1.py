import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

rdd_1=spark.sparkContext.parallelize(("wild", "blackhawks", "red wings", "wild", "oilers", "whalers", "jets","wild"))
rdd_2=rdd_1.map(lambda k: (k, 1))
count_by_key=rdd_2.countByKey()
count_by_key_tuple_list=count_by_key.items()

print(f'The count is:{count_by_key}')
print(f'The count is in tuples way:{count_by_key_tuple_list}')
