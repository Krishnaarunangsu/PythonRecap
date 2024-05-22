# PySpark — Partition: Overwrite Mode:dynamic
# Overwrite only affected partitions without affecting all other data
import pyspark, os, sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, count, lit

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('answer').getOrCreate()

# Setting the partitionOverwriteMode as DYNAMIC
spark.conf.set("spark.sql.sources.partitionOverwriteMode", "dynamic")
spark.conf.get("spark.sql.sources.partitionOverwriteMode")

_data=[
        ["ORD1001", "P003", 70, "01-21-2022"],
        ["ORD1004", "P033", 12, "01-24-2022"],
        ["ORD1005", "P036", 10, "01-20-2022"],
        ["ORD1002", "P016", 2, "01-10-2022"],
        ["ORD1003", "P012", 6, "01-10-2022"]
]
_cols=["order_id","prod_id", "qty", "order_date"]

# Create the dataframe
df=spark.createDataFrame(data=_data, schema=_cols)

# cast the Order Data from String to Data
df=df.withColumn("order_date", to_date("order_date", "MM-dd-yyyy"))
df.printSchema()
df.show()

# Check mode for partition Overwrite
partition_overwrite_mode=spark.conf.get("spark.sql.sources.partitionOverwriteMode")
print(f'Partition Overwrite Mode:{partition_overwrite_mode}')

# Lets repartition the data with order_date and write
df.repartition("order_date") \
    .write \
    .format("parquet") \
    .partitionBy("order_date") \
    .mode("overwrite") \
    .save("orders_partitioned_1")

spark.read.parquet("orders_partitioned_1/").groupby("order_date").agg(count(lit(1))).show()

