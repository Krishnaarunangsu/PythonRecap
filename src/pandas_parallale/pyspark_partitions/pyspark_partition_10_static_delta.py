# PySpark — Dynamic Partition
# Overwrite only affected partitions without affecting all other data
import pyspark, os, sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, count, lit

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('answer').getOrCreate()

# Lets create our delta dataset for Overwrite
_data = [
    ["ORD1010", "P053", 78, "01-24-2022"],
    ["ORD1011", "P076", 21, "01-20-2022"],
]
_cols = ["order_id", "prod_id", "qty", "order_date"]
# Create the delta dataframe
delta_df = spark.createDataFrame(data=_data, schema=_cols)
# Cast the Order date from String to Date
delta_df = delta_df.withColumn("order_date", to_date("order_date" ,"MM-dd-yyyy"))
delta_df.printSchema()
delta_df.show()

# Let's write to the same location for Orders partitioned
delta_df.repartition("order_date") \
    .write \
    .format("parquet") \
    .partitionBy("order_date") \
    .mode("overwrite") \
    .save("orders_partitioned_1")

spark.read.parquet("orders_partitioned_1/").groupby("order_date").agg(count(lit(1))).show()

