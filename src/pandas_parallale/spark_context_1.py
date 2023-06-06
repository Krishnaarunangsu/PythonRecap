import pyspark
from pyspark import SparkContext
import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

sc = SparkContext("local", "First App")

# https://sparkbyexamples.com/hadoop/hadoop-unable-to-load-native-hadoop-library-for-your-platform-warning/
logFile = "C://Spark//spark-3.1.3-bin-hadoop3.2//README.md"
logData = sc.textFile(logFile).cache()
# print(logData.values())
numAs = logData.filter(lambda s: 'a' in s).count()
print(f'The number of As:{numAs}')

numBs =logData.filter(lambda s: 'b' in s).count()
print(f'The number of Bs:{numBs}')
