import os,sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import count,avg,mean

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark=SparkSession.builder.appName('PySpark-Dataframe Group By').getOrCreate()

# Data
dataset={
         'A': [1, 1, 2, 2],
         'B': [1, 2, 3, 4],
         'C': [0.362, 0.227, 1.267, -0.562]
         }

# specify column names
columns = ['A', 'B', 'C']

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(dataset, columns)
dataframe.show()

# Groupby with DEPT with sum() , min() , max()
#aggregated = dataframe.groupby('A').agg('min')
#aggregated.show()



