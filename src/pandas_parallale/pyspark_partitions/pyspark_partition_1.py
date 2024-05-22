from pyspark.sql import SparkSession
import sys
import os

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

#Create Spark Session
spark=SparkSession.builder.appName("SparkTutorial").getOrCreate()

#Schema
schema=["employee_name","department", "state", "sales", "age", "salary"]
# Data
simple_data=[
    ('James', 'Sales', 'NY',90000, 34, 10000),
('Michael', 'Sales', 'NY',86000, 56, 20000),
('Robert', 'Sales', 'CA',81000, 30, 23000),
('Maria', 'Finance', 'CA',90000, 24, 23000),
('Raman', 'Finance', 'CA',99000, 40, 24000),
('Scott', 'Finance', 'NY',83000, 36, 19000),
('Jen', 'Finance', 'NY',79000, 53, 15000),
('Jeff', 'Marketing', 'CA',80000, 25, 18000),
('Kumar', 'Marketing', 'CA',91000, 50, 21000)
]

#Create Spark Dataframe
df=spark.createDataFrame(data=simple_data, schema=schema)

#Dataframe
df.show()

# Repartition ny number
df2=df.repartition(numPartitions=3)
print(f'NumPartitions-Partition by Number of partitions:{df2.rdd.getNumPartitions()}')

#Write Dataframe to CSV file
#df.write.csv(os.path.join(tempfile.mkdtemp(), 'data'))
#df.write.csv("C://Arunangsu/PythonRecap/data/csv/employee_dept.csv")

# Repartition by Single Column
df2=df.repartition('state')
print(f'NumPartitions-Partition by Single Column:{df2.rdd.getNumPartitions()}')

# Repartition by Multiple Columns
df2=df.repartition('state', 'department')
print(f'NumPartitions-Partition by Multiple Column:{df2.rdd.getNumPartitions()}')


