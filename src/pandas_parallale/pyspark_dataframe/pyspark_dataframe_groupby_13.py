import os,sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import count,avg,mean

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark=SparkSession.builder.appName('PySpark-Dataframe Group By').getOrCreate()

# Data
dataframe=spark.createDataFrame([
    {"deptId": 1, "age": 40, "name": "Hyukjin Kwon", "gender": "M", "salary": 50},
    {"deptId": 1, "age": 50, "name": "Takuya Ueshin", "gender": "M", "salary": 100},
    {"deptId": 2, "age": 60, "name": "Xinrong Meng", "gender": "F", "salary": 150},
    {"deptId": 3, "age": 20, "name": "Haejoon Lee", "gender": "M", "salary": 200}
])

dataframe.show()

# Groupby with DEPT with sum() , min() , max()
sum_sal = dataframe.groupby('gender').sum('salary')
sum_sal.show()

aggregated = dataframe.groupby('gender').agg({'salary':'sum'})
aggregated.show()


