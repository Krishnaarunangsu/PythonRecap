import sys
import os
from pyspark.sql import Row, SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()


def calc_range(x):
    list_1 = []
    for i in range(x):
        list_1.append(i)

    return list_1


# returns a new RDD by applying a function to each element of the RDD.
# Function in map can return only one item.

# RDD Transformation
def map_transformation(list_num: list) -> int:
    first_number = None
    try:
        print(f'The input list is:{list_num}')
        rdd_1 = spark.sparkContext.parallelize(list_num)
        # rdd_1.foreach(print)
        print(rdd_1.map(lambda x: (x, x * x)).collect())
        #print(rdd_1.map(calc_range).collect())
        rdd_2=rdd_1.map(calc_range)
        #rdd_2 = spark.sparkContext.parallelize([1, 2, 3])
        #print(rdd_2.map(lambda x: (x, x * x)).collect())
        # data_collected_rdd=spark.sparkContext.parallelize([3, 4, 5]).map(lambda x: range(1, x)).collect()
        data_collected_rdd = rdd_2.collect()
        return data_collected_rdd
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
    # list_1 = []
    if len(list_1) == 0:
        raise ValueError('Input List is Empty')
    data_collected = map_transformation(list_1)
    print(f'generated data is:{data_collected}')
