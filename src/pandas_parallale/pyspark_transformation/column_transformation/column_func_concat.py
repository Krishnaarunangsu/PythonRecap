import os,sys
import pyspark
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import sum, count, avg, mean, max, expr, log, concat, lit, split

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

employee_dataframe=employee_dataframe.withColumn("fullname", concat(employee_dataframe["firstname"],lit(" "),employee_dataframe["middlename"],lit(" "),employee_dataframe["lastname"]))
employee_dataframe_updated=employee_dataframe.drop("firstname","middlename","lastname" )
employee_dataframe_updated.show()

columns = ["firstname", "middlename", "lastname"]
employee_dataframe_updated = employee_dataframe_updated.withColumn("fullname", split(employee_dataframe_updated["fullname"], " "))
for i, column in enumerate(columns):
    employee_dataframe_updated = employee_dataframe_updated.withColumn(column, employee_dataframe_updated["fullname"][i])
employee_dataframe_updated = employee_dataframe_updated.drop("fullname")
employee_dataframe_updated.show()