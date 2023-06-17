import os
import sys
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row, SparkSession
from pyspark.sql.functions import col

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkExample_1').getOrCreate()
# df = spark.createDataFrame([
#     Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
#     Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
#     Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
# ])

data_1=[
    ("James", ["Java", 'Scala'],{'hair':'black', 'eye':'brown'}),
("James", ["Java", 'Scala'],{'hair':'black', 'eye':'brown'}),
("James", ["Java", 'Scala'],{'hair':'black', 'eye':'brown'}),
("Washington", None,None),
("Jefferson", ["1", '2'],{}),
]

schema=['name', 'known_languages', 'properties']

df = spark.createDataFrame(data=data_1, schema = ['name','knownLanguages','properties'])
df.show()
