import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()


# returns a new RDD by applying a function to each element of the RDD.
# Function in map can return only one item.

# RDD Transformation
def map_transformation(list_num: list) -> int:
    first_number = None
    try:
        print(f'The input list is:{list_num}')
        rdd_1 = spark.sparkContext.parallelize(list_num)
        print('Each element of the RDD is:')
        rdd_1.foreach(print)
        first_number = rdd_1.first()
        return first_number
    except ValueError as ve:
        raise ValueError('Input List is Empty')

    # if len(list_num) > 0:
    #     print(list_num)
    #     rdd_1 = spark.sparkContext.parallelize(list_num)
    #     first_number = rdd_1.first()
    # else:
    #     raise ValueError("RDD is Empty")


if __name__ == "__main__":
    list_1 = [3, 4, 5]
    #list_1 = []
    if len(list_1) ==0:
        raise ValueError('Input List is Empty')
    first_num = map_transformation(list_1)
    print(f'The first number is:{first_num}')
