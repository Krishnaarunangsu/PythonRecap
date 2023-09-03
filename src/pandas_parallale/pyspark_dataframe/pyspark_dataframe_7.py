import os
import sys
from datetime import datetime, date
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('Jagannath').getOrCreate()

#Student=Row("firstName","lastName","email","age","rollNumber")
person_data=[]
try:
    person_data = [
        Row(name='James, Smith', prop=Row(hair='Black', eye='Blue')),
                    Row(name='Michael, Ross', prop=Row(hair='Grey', eye='Black'))
                    ]
    # student_data=[Student('James, Smith',['Java','Scala','C++'], state='CA'),
    #           Student('Michael, Rose',['Spark','Java','C++'], state='NJ'),
    #           Student('Robert, Williams',['CSharp','VB'], state='NV')]

except TypeError as te:
    print(f'Wrong Keyword:{te}')
print(len(person_data))
print('***********************************************************')
# Changing the Dataframe Columns
person_df=spark.createDataFrame(person_data)
print(f'Person Dataframe Metadata')
person_df.printSchema()
print('***********************************************************')
print(f'First few records of the Student Dataframe:{person_df.head()}')
print('***********************************************************')
print(f'Records of the Student Dataframe')
{person_df.show()}
# df = spark.createDataFrame([
#     Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
#     Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
#     Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
# ])
# print(df.head())
# print(df.show())