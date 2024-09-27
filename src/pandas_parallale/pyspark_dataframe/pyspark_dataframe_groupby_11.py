import os,sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum,count,avg,mean, max

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark=SparkSession.builder.appName('PySpark-Dataframe Group By').getOrCreate()

# Data
dataset=[["1", "sravan", "IT", 45000],
        ["2", "ojaswi", "CS", 85000],
        ["3", "rohith", "CS", 41000],
        ["4", "sridevi", "IT", 56000],
        ["5", "bobby", "ECE", 45000],
        ["6", "gayatri", "ECE", 49000],
        ["7", "gnanesh", "CS", 45000],
        ["8", "bhanu", "Mech", 21000]
        ]

# specify column names
columns = ['ID', 'NAME', 'DEPT', 'FEE']

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(dataset, columns)

# Groupby with DEPT with sum() , min() , max()
#dataframe.groupBy("DEPT").agg(max("FEE"), sum("FEE"),min("FEE"), mean("FEE"),count("FEE")).show()
aggregated_sum=dataframe.groupBy("DEPT").agg(sum("FEE"))
aggregated_sum.show()

aggregated_max=dataframe.groupBy("DEPT").agg(max("FEE"))
aggregated_max.show()



