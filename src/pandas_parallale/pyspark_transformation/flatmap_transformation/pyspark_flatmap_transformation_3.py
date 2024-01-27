# flatMap is similar to map, because it applies a function to all elements in a RDD.  But, flatMap flattens the results.
import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()
data_1 = [
    "This is an sample application to see the FlatMap operation in PySpark"
]
rdd_1 = spark.sparkContext.parallelize(data_1)
# print(rdd_1) # does not show anything
data_col_1 = rdd_1.collect()
print(f'Original RDD:{data_col_1}')
# for row in data_col_1:
#     print(row)
print('***********************Flatmap Transformation*****************************')
rdd_2 = rdd_1.flatMap(lambda x: x.split(" "))
print('The RDD is:')
rdd_2.foreach(print)
print("######################################################")
# Return a list that contains all the elements in this RDD.
# This method should only be used if the resulting array is expected to be small,
# as all the data is loaded into the driver’s memory.
data_col_2 = rdd_2.collect()
print(f'RDD after flatMap Transformation:{data_col_2}')
print('-----------------------------------------------------')
for row in data_col_2:
    print(row)
print('-----------------------------------------------------')
print('**********************Map Transformation******************************')

rdd_3 = rdd_1.map(lambda x: x.split(" "))

# Return a list that contains all the elements in this RDD.
# This method should only be used if the resulting array is expected to be small,
# as all the data is loaded into the driver’s memory.
data_col_3 = rdd_3.collect()
print(f'RDD after map Transformation:{data_col_3}')
print('-----------------------------------------------------')
for row in data_col_3:
    print(row)
print('-----------------------------------------------------')
