# flatMap is similar to map, because it applies a function to all elements in a RDD.  But, flatMap flattens the results.
import sys
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark= SparkSession.builder.appName("Spark-Dataframe").getOrCreate()
data_1=[
    ("James", ["Java", 'Scala'],{'hair':'black', 'eye':'brown'}),
("Michael", ["Java", 'Scala'],{'hair':'black', 'eye':'brown'}),
("Robert", ["Java", 'Scala'],{'hair':'black', 'eye':'brown'}),
("Washington", None,None),
("Jefferson", ["1", '2'],{}),
]
schema=['name', 'known_languages', 'properties']
# convert data todataframe
data_frame_1=spark.createDataFrame(data=data_1, schema=schema)
# This example flattens the array column “knownLanguages” and yields below output
data_frame_2=data_frame_1.select(data_frame_1.name, explode(data_frame_1.known_languages))
data_frame_2.printSchema()
data_frame_2.show(truncate=False)
