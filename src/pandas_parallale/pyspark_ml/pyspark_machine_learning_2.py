import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("answers").getOrCreate()

path = "Fortune 500 Companies US.csv"

df = spark.read.option("header",'True').option('delimiter', ',').csv(path)
df.printSchema()

print(df.head())
print(df.show())