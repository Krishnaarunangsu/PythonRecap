import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()

# rdd_1=spark.sparkContext.parallelize(("wild", "blackhawks", "red wings", "wild", "oilers", "whalers", "jets","wild"))
#rdd_1.map(lambda k: (k,1)).countByKey().items()
# rdd_2.saveAsTextFile('..//..//..//..//data//csv//hockey_teams.txt')
rdd_1= spark.sparkContext.parallelize(range(10)).saveAsTextFile('py_actions')



