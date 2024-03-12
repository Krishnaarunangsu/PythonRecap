# RDD.flatMapValues(f: Callable[[V], Iterable[U]]) → pyspark.rdd.RDD[Tuple[K, U]]
# Pass each value in the key-value pair RDD through a flatMap function without changing the keys;
# this also retains the original RDD’s partitioning.

# Parameters: f: function
#               a function to turn a V into a U

# Returns: RDD
#          a RDD containing the keys and the mapped value

import sys
import os
from pyspark.sql import SparkSession

@staticmethod
def process(x)->any:
    """

    Args:
        x:

    Returns: any
             the flattened array

    """
    return x


class FlatMapValuesTransformation:
    """
    MapValues Transformation
    """
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
    spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()
    def __init__(self,fruit_data:tuple):
        """

        Args:
            fruit_data: tuple
        """
        self.fruit_data=fruit_data

    def create_rdd(self):
        """

        Returns: rdd
                 RDD with mapValues Transformation on the values of the key-value pairs

        """
        # rdd_key_value=FlatMapValuesTransformation.spark.sparkContext.parallelize(self.fruit_data)
        rdd_key_value = self.spark.sparkContext.parallelize(self.fruit_data)
        print(f'RDD from the list of tuples:{rdd_key_value.collect()}')
        print('***********Flatten the values of each key******')
        rdd_map_values=rdd_key_value.flatMapValues(process).collect()
        return rdd_map_values


if __name__=="__main__":
    tuple_list:list=[("a", ["apple", "banana", "lemon"]), ("b", ["grapes", "oranges"])]
    flatMap_values_transformation=FlatMapValuesTransformation(tuple_list)
    transformed_records=flatMap_values_transformation.create_rdd()
    print(f'Transformed Values:\n{transformed_records}')