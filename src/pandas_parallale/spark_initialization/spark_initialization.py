#Spark Initialization Module

import os,sys
import pyspark
from pyspark.sql import SparkSession
class SparkInitialization:
    """
    Class for Spark Initialization
    """

    def __init__(self):
        """
        Initialization
        """
        os.environ['PYSPARK_PYTHON'] = sys.executable
        os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
        self.spark=None

    def get_spark_object(self)->SparkSession:
        """

        Returns:

        """

        spark = SparkSession.builder.appName('PySpark-Example').getOrCreate()
        return spark

