import sys
import os
from pyspark.sql import SparkSession
class NarrowTransformationSquaredRDD:
    """
    Narrow Transformation for squaring a RDD
    """
    os.environ['PYSPARK_PYTHON']=sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON']=sys.executable
    spark=SparkSession.builder.appName("Narrow Transformation").getOrCreate()
    def __init__(self):
        """
        Initialization
        Args:
            input_data:
        """
        self.input_data=None
        self.original_rdd=None
        self.transformed_squared_rdd=None

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

    def squared_transformed_rdd(self,input_dataset:list):
        """

        Returns:

        """
        self.create_original_rdd(input_dataset)
        self.transformed_squared_rdd=self.original_rdd.map(lambda x: x**2)
        #print(f'The transformed Squared RDD is:{self.transformed_squared_rdd.collect()}')
        print('The transformed Squared RDD is:')
        self.display(self.transformed_squared_rdd)



if __name__=="__main__":
    narrow_transform_square_rdd=NarrowTransformationSquaredRDD()
    # Input Data
    dataset=[1, 2, 3]
    # narrow_transform_square_rdd.create_original_rdd(dataset)
    narrow_transform_square_rdd.squared_transformed_rdd(dataset)