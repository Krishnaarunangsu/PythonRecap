import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

# create student marks data with 20 elements

student_marks = spark.sparkContext.parallelize(
     [89, 76, 78, 89, 90, 100, 34, 56, 54, 22, 45, 43, 23, 56, 78, 21, 34, 34, 56, 34])

# display data in RDD

student_marks_flatmap=student_marks.flatMap(lambda x:[x, x, x] )
print(f'Data in flatMap RDD:{student_marks_flatmap.collect()}')

print(f'Data in RDD: {student_marks.map(lambda element: element).collect()}')

# Apply filter() transformation by returning only multiples of 5.

print(f'Multiples of 5 from an RDD: {student_marks.filter(lambda element: element % 5 == 0).collect()}')
