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

    # retrieving the data from the dataframe using collect()
    # This becomes a list but not flattened
    dataframe_2 = dataframe_1.collect()
    print(f"Retrieved Data is:-{dataframe_2}")
    print(f'Size:{len(dataframe_2)}')

    print("Retrieved Data is:-")

    # Retrieving multiple rows using collect() and for loop
    for row in dataframe_1.collect()[0:2]:
        print((row["State"]), ",", str(row["Cases"]), ",",
              str(row["Recovered"]), ",", str(row["Deaths"]))

    # Retrieving data from 0th row
    print(f'0th Row of the Dataframe:{dataframe_1.collect()[0][0:]}')

    print("Retrieved Data is:-")

    # Retrieving data of the "State","Recovered" and "Deaths" column
    for col in dataframe_1.collect():
        print(col["State"], ",", col["Recovered"], ",",col["Deaths"])

    # convert particular column to list using flatMap and check the presence of a value
    value_existence="Uttar Pradesh"
    print(dataframe_1.select('State').
          rdd.flatMap(lambda x: x).collect().count(value_existence))

    # convert student Name to list using flatMap
    print(dataframe_1.select('Cases').
          rdd.flatMap(lambda x: x).collect())

    # convert student ID to list using flatMap
    print(dataframe_1.select('Recovered').
          rdd.flatMap(lambda x: x).collect())

    # raise converted from None
    # pyspark.sql.utils.AnalysisException: cannot resolve '`Death`'
    print(dataframe_1.select('Deaths').
          rdd.flatMap(lambda x: x).collect())

    # convert multiple columns  to list using flatMap
    column_list=['State','Cases','Recovered','Deaths']
    print(dataframe_1.select(column_list).
          rdd.flatMap(lambda x: x).collect())

    # convert  student Name  to list using map
    print(dataframe_1.select('State').
          rdd.map(lambda x: x['State']).collect())

    print(dataframe_1.select('*').
          rdd.map(lambda x: x['State']).collect())

    print(dataframe_1.select('*').
          rdd.map(lambda x: x[1]).collect())

    print(dataframe_1.select('State').
          rdd.map(lambda x: x[0]).collect())

    # convert  student ID  to list using map
    print(dataframe_1.select('Cases').
          rdd.map(lambda x: x[0]).collect())

    # convert  student college  to list using
    # map
    print(dataframe_1.select('Recovered').
          rdd.map(lambda x: x[0]).collect())


