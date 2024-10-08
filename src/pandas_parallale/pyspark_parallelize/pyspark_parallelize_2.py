import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
# Creates a Spark Session
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

list_tuples=([('Monkey,12'),('Aug, 13'),('Raiff', 45), ('Bob', 10), ('Scott', 47)])

# Convert the list into RDD
# rdd_1=spark.sparkContext.parallelize(list_data_1, 4)
rdd_1=spark.sparkContext.parallelize(list_tuples)

# Pick the first element of the RDD
print(f'The first element of the RDD is:{rdd_1.first()}')
