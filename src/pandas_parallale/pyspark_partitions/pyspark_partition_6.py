# Range Partition
import pyspark, os, sys
from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('answer').getOrCreate()

# Create Sample Dataframe
path="C://Arunangsu//PythonRecap//data//csv//Cricket_data_set_odi.csv"
df=spark.read.option("header", True).csv(path)

# Display schema
df.printSchema()


# From above DataFrame, we will be using
# Team and Speciality as a partition key
# for our examples below.
# partitionBy()
df.write.option("header", True) \
        .partitionBy("Team", "Speciality") \
        .mode("overwrite") \
        .csv("Team-Speciality")