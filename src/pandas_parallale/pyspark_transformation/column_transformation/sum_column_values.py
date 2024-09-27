import os,sys
import pyspark
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import sum,count,avg,mean, max, expr

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# data
data = [('James','','Smith','1991-04-01','M',3000, 1000),
  ('Michael','Rose','','2000-05-19','M',4000, 1500),
  ('Robert','','Williams','1978-09-05','M',4000, 1500),
  ('Maria','Anne','Jones','1967-12-01','F',4000, 1500),
  ('Jen','Mary','Brown','1980-02-17','F',-1, 0)
]
columns = ["firstname","middlename","lastname","dob","gender","salary", "bonus"]

spark=SparkSession.builder.appName('Spark With columns').getOrCreate()
employee_dataframe=spark.createDataFrame(data, schema=columns)
print('Original Dataframe')
employee_dataframe.show()
# Add a new column compensation by summing salary and bounus
#employee_dataframe=employee_dataframe.withColumn("compensation", sum(employee_dataframe["salary"], employee_dataframe["bonus"]))
print('Dataframe with Numeric columns sum')
employee_dataframe_sum: DataFrame=employee_dataframe.groupby().sum()
employee_dataframe_sum.show()
salary_sum=employee_dataframe_sum.collect()[0][0]
print(f'Sum of the salary:{salary_sum}')
bonus_sum=employee_dataframe_sum.collect()[0][1]
print(f'Sum of the bonus:{bonus_sum}')

employee_dataframe_gender_sum: DataFrame=employee_dataframe.groupby("gender").sum()
employee_dataframe_gender_sum.show()

