import pyspark, os, sys
from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('answer').getOrCreate()

data = [("James","Educative","Engg","USA"),
    ("Michael","Google",None,"Asia"),
    ("Robert",None,"Marketing","Russia"),
    ("Maria","Netflix","Finance","Ukraine"),
    (None, None, None, None)
  ]

columns = ["emp name","company","department","country"]
df = spark.createDataFrame(data = data, schema = columns)

csv_file_path = "data.csv"
df.write.option("header", True).option("delimiter",",").csv(csv_file_path)