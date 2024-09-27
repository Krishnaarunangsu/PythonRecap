import os,sys
import pyspark
from pyspark.sql import SparkSession
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
employee_dataframe.show()
# Add a new column compensation by summing salary and bounus
#employee_dataframe=employee_dataframe.withColumn("compensation", sum(employee_dataframe["salary"], employee_dataframe["bonus"]))
employee_dataframe=employee_dataframe.withColumn("compensation", expr("salary+bonus"))
employee_dataframe.show()
