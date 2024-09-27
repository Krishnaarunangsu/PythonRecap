import sys
import os
from pyspark.sql import SparkSession
class WideTransformationRDD:
    """
    Narrow Transformation for squaring a RDD
    """
    os.environ['PYSPARK_PYTHON']=sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON']=sys.executable
    spark=SparkSession.builder.appName("Wide Transformation").getOrCreate()
    def __init__(self):
        """
        Initialization
        Args:
            input_data:
        """
        self.input_data=None
        self.original_rdd=None
        self.transformed_groupby_rdd_count=None
        self.transformed_reducyby_item_list = None

    @staticmethod
    def display(rdd):
        """
        Display the RDD
        Returns:

        """
        print(rdd.collect())
    def create_original_rdd(self,input_data:list):
        """

        Returns:

        """
        self.input_data = input_data
        self.original_rdd=self.spark.sparkContext.parallelize(self.input_data)
        # print(f'The Original RDD is:\n{self.original_rdd.collect()}')
        print('The Original RDD is:')
        self.display(self.original_rdd)
        #self.original_rdd.display()

    def reducebykey_transformed_rdd(self,input_dataset:list):
        """

        Returns:

        """
        # Create RDD from the input dataset
        self.create_original_rdd(input_dataset)
        self.transformed_reducyby_item_list=self.original_rdd.reduceByKey(lambda x,y: x+y)
        # Wide Transformation :reduceByKey
        self.display(self.transformed_reducyby_item_list)




if __name__=="__main__":
    narrow_transform_square_rdd=WideTransformationRDD()
    # Input Data
    dataset=[("Alice", 1), ("Bob", 2), ("Charlie", 3), ("Alice", 4), ("Bob", 5)]
    # narrow_transform_square_rdd.create_original_rdd(dataset)
    narrow_transform_square_rdd.reducebykey_transformed_rdd(dataset)