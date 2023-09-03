import sys
import os
from pyspark.sql import Row, SparkSession
from pyspark.sql.functions import col


os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.master("local[1]").appName('SparkExample_1').getOrCreate()


data = Row(
      ("James","Smith","USA","CA"),
      ("Michael","Rose","USA","NY"),
      ("Robert","Williams","USA","CA"),
      ("Maria","Jones","USA","FL")
      )
columns = ["firstname","lastname","country","state"]

person_df = spark.createDataFrame(data).toDF(*columns)
print('Person Dataframe')
person_df.show()
print('****************************************************')
print('Session-Scoped Temporary Table')
# Create Temporary View/Table
person_df.createOrReplaceTempView("Person")


# Run SQL Query
spark.sql("select firstname, lastname from Person").show()



