import os,sys
import pyspark
from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# function to create new Spark Session
def create_spark_session():
    """
    Create the spark session
    Returns:

    """
    spark_session=SparkSession.builder.appName('PySpark-Dataframe').getOrCreate()
    return spark_session

# function to create SparkContext
def create_spark_context(spark_session:SparkSession):
    """

    Args:
        spark_session:

    Returns:
        spark_context

    """
    spark_context=spark_session.sparkContext
    return spark_context

# Create RDD from dataset
def create_RDD(spark_context:SparkSession.sparkContext,data):
    """

    Args:
        spark_context:
        data:

    Returns:
        rdd: RDD[T]

    """
    rdd=spark_context.parallelize(data)
    return rdd

# Create Dataframe from RDD
def create_dataframe(spark_session:SparkSession, rdd, columns:list):
    """

    Args:
        spark_session:
        rdd:
        columns:

    Returns:

    """
    df=spark_session.createDataFrame(rdd,columns)
    return df


if __name__ == "__main__":

    # Dataset
    input_data = [("Uttar Pradesh", 122000, 89600, 12238),
                  ("Maharashtra", 454000, 380000, 67985),
                  ("Tamil Nadu", 115000, 102000, 13933),
                  ("Karnataka", 147000, 111000, 15306),
                  ("Kerala", 153000, 124000, 5259)]
    #Columns
    schema_lst = ["State", "Cases", "Recovered", "Deaths"]

    # calling function to create SparkSession
    spark = create_spark_session()

    # creating spark context object
    sc = create_spark_context(spark)

    # calling function to create RDD
    rdd_1 = create_RDD(sc, input_data)

    # calling function to create Dataframe
    dataframe_1=create_dataframe(spark,rdd_1,schema_lst)

    # printing schema of the dataframe and showing the dataframe
    dataframe_1.printSchema()
    dataframe_1.show()
    print(f'Dataframe Count:{dataframe_1.count()}')

# display college column in
# the list format using comprehension
print([data[0] for data in dataframe_1.
      select('State').collect()])

# display student ID column in the
# list format using comprehension
print([data[0] for data in dataframe_1.
      select('Cases').collect()])

# display subject1  column in the list
# format using comprehension
print([data[0] for data in dataframe_1.
      select('Recovered').collect()])

# display subject2  column in the
# list format using comprehension
print([data[0] for data in dataframe_1.
      select('Deaths').collect()])

print([data[1] for data in dataframe_1.
      select('*').collect()])

print([(data[1],data[2]) for data in dataframe_1.
      select('*').collect()])

print([(data[1],data[2]) for data in dataframe_1.
      select('*').collect()])