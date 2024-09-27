import os,sys
import pyspark
from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark=SparkSession.builder.appName('PySpark-Dataframe Group By').getOrCreate()

# Data
dataset=[
("James","Sales","NY",90000,34,10000),
    ("Michael","Sales","NY",86000,56,20000),
    ("Robert","Sales","CA",81000,30,23000),
    ("Maria","Finance","CA",90000,24,23000),
    ("Raman","Finance","CA",99000,40,24000),
    ("Scott","Finance","NY",83000,36,19000),
    ("Jen","Finance","NY",79000,53,15000),
    ("Jeff","Marketing","CA",80000,25,18000),
    ("Kumar","Marketing","NY",91000,50,21000)
]

# Schema
columns=["employee_name", "department", "state", "salary", "age", "bonus"]

# Create the Dataframme
df=spark.createDataFrame(dataset, schema=columns)
print(f'The Dataframe Schema is:\n')
df.printSchema()
print(f'The Dataframe is:\n')
# df.show(truncate=True)
df.show(truncate=False)

# Grouping on the Department
print(f'Sum of Salary for Every Department in the dataset')
df.groupby("department").sum("salary").show()




