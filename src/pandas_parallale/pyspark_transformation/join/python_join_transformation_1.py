import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

names_1 = spark.sparkContext.parallelize(("abe", "abby", "apple")).map(lambda a: (a, 1))
names_2 = spark.sparkContext.parallelize(("apple", "beatty", "beatrice")).map(lambda a: (a, 1))

inner_join_names_1_names_2=names_1.join(names_2).collect()

print(f'Inner Join of Names: {inner_join_names_1_names_2}')

left_outer_join_names_1_names_2=names_1.leftOuterJoin(names_2).collect()

print(f'Left Outer Join of Names: {left_outer_join_names_1_names_2}')

right_outer_join_names_1_names_2=names_1.rightOuterJoin(names_2).collect()

print(f'Right Outer Join of Names: {right_outer_join_names_1_names_2}')