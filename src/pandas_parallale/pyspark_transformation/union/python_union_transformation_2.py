# import the pyspark module
import os
import sys

import pyspark

# import SparkSession for creating a session

from pyspark.sql import SparkSession

# import RDD from pyspark.rdd

from pyspark.rdd import RDD

# create an app named linuxhint
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark_app = SparkSession.builder.appName('linuxhint').getOrCreate()

# create student marks data with 20 elements

student_marks1 = spark_app.sparkContext.parallelize(range(1,10))

# create student marks data with 10 elements

student_marks2 = spark_app.sparkContext.parallelize(range(10, 21))

# display data in RDD

print(f'Actual data in student marks 1 RDD: {student_marks1.map(lambda element: element).collect()}')

# display data in RDD

print(f'Actual data in student marks 2 RDD: {student_marks2.map(lambda element: element).collect()}' )

# Apply union() transformation by performing union on the above 2 RDD's

print(f'Union Transformation on two RDD : {student_marks1.union(student_marks2).collect()}')