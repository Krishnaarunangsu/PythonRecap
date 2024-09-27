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
        self.transformed_groupby_item_list = None

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

    def groupby_transformed_rdd(self,input_dataset:list):
        """

        Returns:

        """
        # Create RDD from the input dataset
        self.create_original_rdd(input_dataset)

        # Group By Key and have the item count for each key
        self.transformed_groupby_rdd_count = self.original_rdd.groupByKey().mapValues(len)
        # Group By Key and have the item list for each key
        self.transformed_groupby_item_list=self.original_rdd.groupByKey().mapValues(list)
        #self.transformed_groupby_rdd_count = self.original_rdd.groupByKey().mapValues(len).collect()
        #self.transformed_groupby_item_list = self.original_rdd.groupByKey().mapValues(list).collect()
        #print(f'The Group By RDD Item Count is:{self.transformed_groupby_rdd_count}')
        #print(f'The Group By RDD Item List is:{self.transformed_groupby_item_list}')
        print('The Group By RDD Item Count is')
        self.display(self.transformed_groupby_rdd_count)
        print('The Group By RDD Item List is')
        self.display(self.transformed_groupby_item_list)



if __name__=="__main__":
    narrow_transform_square_rdd=WideTransformationRDD()
    # Input Data
    dataset=[("apple", 3),("orange", 2),("apple",5), ("orange", 4)]
    # narrow_transform_square_rdd.create_original_rdd(dataset)
    narrow_transform_square_rdd.groupby_transformed_rdd(dataset)