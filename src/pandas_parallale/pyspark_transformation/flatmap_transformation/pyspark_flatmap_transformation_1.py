# flatMap is similar to map, because it applies a function to all elements in a RDD.  But, flatMap flattens the results.
import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()
data_1=[2, 3, 4]
rdd_1=spark.sparkContext.parallelize(data_1)
# print(rdd_1) # does not show anything
data_col_1=rdd_1.collect()
print(f'Original RDD:{data_col_1}')
# for row in data_col_1:
#     print(row)
print('****************************************************')
rdd_2=rdd_1.flatMap(lambda x: [x,x,x])
data_col_2=rdd_2.collect()
print(f'RDD after flatMap Transformation:{data_col_2}')
print('****************************************************')

rdd_3=rdd_1.map(lambda x: [x,x,x])
data_col_3=rdd_3.collect()
print(f'RDD after map Transformation:{data_col_3}')