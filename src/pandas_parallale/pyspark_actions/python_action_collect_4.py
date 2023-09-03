import os
import sys
from datetime import datetime, date
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('Jagannath').getOrCreate()

#  Create Empty Student Class-Metadata
Student=Row('name','language','state')
#Student=Row("firstName","lastName","email","age","rollNumber")
student_data=[]
try:
    student_data = [Student('James, Smith', ['Java', 'Scala', 'C++'], 'CA'),
                    Student('Michael, Rose', ['Spark', 'Java', 'C++'], 'NJ'),
                    Student('Robert, Williams', ['CSharp', 'VB'], 'NV')]
    # student_data=[Student('James, Smith',['Java','Scala','C++'], state='CA'),
    #           Student('Michael, Rose',['Spark','Java','C++'], state='NJ'),
    #           Student('Robert, Williams',['CSharp','VB'], state='NV')]

except TypeError as te:
    print(f'Wrong Keyword:{te}')
print(len(student_data))
student_rdd=spark.sparkContext.parallelize(student_data)

student_rdd_col=student_rdd.collect()
for row in student_rdd_col:
    try:
        print(f'Name:{row[0]},Programming Language:{row[1]}')
    except IndexError as ie:
        print(f'Error Has occurred:{ie}')
        print(f'Error Has occurred:{ie.args}')
    try:
        print(f'Name:{row.name},Programming Language:{row.language}')
    except AttributeError as ae:
        print(f'Error Has occurred:{ae}')
        print(f'Error Has occurred:{ae.args}')
    finally:
        print('********************************************')



# df = spark.createDataFrame([
#     Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
#     Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
#     Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
# ])
# print(df.head())
# print(df.show())