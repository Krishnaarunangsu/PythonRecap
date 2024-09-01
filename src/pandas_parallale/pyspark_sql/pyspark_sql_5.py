import os
import sys
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Create a spark session for DataFrame and SQL work
spark=SparkSession.builder.master("local").appName(" Spark SQL Example").getOrCreate()
print(f'Spark Object:\n{spark}')
# For an existing SparkConf, use conf parameter.
spark_config_1=SparkSession.builder.config(conf=SparkConf())
print(f'SparkConfig-1:{spark_config_1}')

# For a (key, value) pair, you can omit parameter names.
spark_config_2=SparkSession.builder.config("spark.some.config.option", "some-value")
print(f'SparkConfig-2:{spark_config_2}')

# spark_config_3=SparkSession.builder.config("k1", "v1").getOrCreate()
# spark_config_comparison=spark_config_3.conf.get("k1")==spark_config_3.sparkContext.getConf().get("k1")=="v1"
s1 = SparkSession.builder.config("k1", "v1").getOrCreate()
print(s1.conf.get("k1")=="v1")
print(s1.sparkContext.getConf().get("k1"))

# In case an existing SparkSession is returned,
# the config options specified in this builder will be applied to the existing SparkSession.
s2 = SparkSession.builder.config("k2", "v2").getOrCreate()
print(s1.conf.get("k1") == s2.conf.get("k1"))
print(s1.conf.get("k2") == s2.conf.get("k2"))
