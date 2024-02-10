import os
import sys
from datetime import datetime, date
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('Jagannath').getOrCreate()

#  Create Empty Student Class-Metadata
Student: Row=Row("firstName","lastName","email","age","rollNumber")
print(len(Student))
print(Student.__len__())

# Create Rows of the Dataframe/Table
student1: Row=Student('Krishna', 'Narayan','xyz@abc.com',100,11122)
student2: Row=Student('Tirupati', 'Vishnu','xyz@abc.com',100,11122)
student3: Row=Student('Kalki', 'Narasimha','xyz@abc.com',100,11122)
student4: Row=Student('Dhananjay', 'Gopal','xyz@abc.com',100,11122)
student5: Row =Student('Hari', 'Jagannath','xyz@abc.com',100,11122)
print(student1.firstName)

student_data=[student1,student2,student3, student4, student5]

# Create RDD from the above List
rdd_student=spark.sparkContext.parallelize(student_data)
print(rdd_student)
print(f'Student Data:{rdd_student.collect()}')
print(rdd_student.flatMap(lambda x:[x]).collect())

# df = spark.createDataFrame([
#     Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
#     Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
#     Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
# ])
# print(df.head())
# print(df.show())