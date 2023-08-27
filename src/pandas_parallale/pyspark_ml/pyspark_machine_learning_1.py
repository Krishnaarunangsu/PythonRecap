from pyspark.conf import SparkConf
from pyspark.context import SparkContext

conf = SparkConf().setAppName('PySpark Demo App').setMaster('local[2]')
conf.get('spark.master')
conf.get('spark.app.name')