import os,sys
import pyspark
from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark=SparkSession.builder.appName('PySpark-Dataframe').getOrCreate()
dept=[('Finance',10), \
      ('Marketing',20), \
      ('Sales',30), \
      ('IT',40)]

deptColumns=['dept_name','dept_id']
# Create Spark Dataframe
deptDF=spark.createDataFrame(data=dept, schema=deptColumns)
deptDF.show(truncate=False)

# Collect the Department records
dataCollect=deptDF.collect()
print('Department Collection')
print(dataCollect)

# Collect the Department Name Column
dataCollect2=deptDF.select('dept_name').collect()
print('Department Name Collection')
print(dataCollect2)

# Iterate the Department Records
print('Department Records')
for row in dataCollect:
    print(f'{row["dept_name"]}:{row["dept_id"]}')