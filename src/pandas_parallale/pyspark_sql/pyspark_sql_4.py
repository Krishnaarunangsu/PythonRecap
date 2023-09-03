import sys
import os
from pyspark.sql import Row, SparkSession



os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


# Create SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com') \
      .getOrCreate()

# Create DataFrame
df = spark.read \
      .option("header", True) \
      .csv("sample_zipcodes.csv")

df.printSchema()
print('*************************************************************')
df.show()
print('*************************************************************')
# Create SQL table
spark.read \
      .option("header", True) \
      .csv("sample_zipcodes.csv") \
      .createOrReplaceTempView("Zipcodes")

# Select query
df.select("country", "city", "zipcode", "state") \
      .show(5)
print('*************************************************************')
spark.sql("SELECT  country, city, zipcode, state FROM ZIPCODES") \
      .show(5)
print('*************************************************************')
# where
df.select("country", "city", "zipcode", "state") \
      .where("state == 'AZ'") \
      .show(5)
print('*************************************************************')
spark.sql(""" SELECT  country, city, zipcode, state FROM ZIPCODES 
          WHERE state = 'AZ' """) \
      .show(5)
print('*************************************************************')
# sorting
df.select("country", "city", "zipcode", "state") \
      .where("state in ('PR','AZ','FL')") \
      .orderBy("state") \
      .show(10)
print('*************************************************************')
spark.sql(""" SELECT  country, city, zipcode, state FROM ZIPCODES 
          WHERE state in ('PR','AZ','FL') order by state """) \
      .show(10)
print('*************************************************************')
# grouping
df.groupBy("state").count() \
      .show()
print('*************************************************************')
spark.sql(""" SELECT state, count(*) as count FROM ZIPCODES 
          GROUP BY state""") \
      .show()
