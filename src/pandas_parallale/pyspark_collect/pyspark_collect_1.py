import sys
import os
from pyspark.sql import Row, SparkSession
from pyspark.sql.functions import col

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Creates a Spark Session
def create_spark_session():
    """
    function to create new SparkSession
    Returns:

    """
    spark = SparkSession.builder.appName('Corona_cases_statewise.com').getOrCreate()
    return spark


def create_spark_context(spark: SparkSession):
    """
    function to initialize SparkContext
    Args:
        spark: SparkSession

    Returns:
        sc: SparkContext

    """

    sc=spark.sparkContext
    return sc


def create_RDD(sc, data):
    """
    Creates a RDD object
    Args:
        sc: SparkContext
        data: List

    Returns:
        object: RDD

    """
    df=sc.parallelize(data)
    return df


def create_data_frame(spark: SparkSession,rdd_df, schema_lst: list):
    """

    Args:
        spark:
        rdd_df:
        schema_lst:

    Returns:Dataframe

    """
    df = spark.createDataFrame(rdd_df,schema_lst)
    return df

if __name__=="__main__":
    state_covid_data=[
                      ("Uttar Pradesh",122000,89600,12238),
                      ("Maharashtra",454000,380000,67985),
                      ("Tamil Nadu",115000,102000,13933),
                      ("Karnataka",147000,111000,15306),
                      ("Kerala",153000,124000,5259)
                      ]
    schema_list = ["State", "Cases", "Recovered","Deaths"]

    # Calling function to create SparkSession
    spark=create_spark_session()

    # Calling function to create SparkContext
    sc=create_spark_context(spark)

    # Calling function to create RDD
    rdd=create_RDD(sc, state_covid_data)

    # Calling Function to create the dataframe from RDD
    df=create_data_frame(spark,rdd,schema_list)

    # Printing the schema of the dataframe and showing the dataframe
    print('****************************************************************')
    print(f'The Schema of the dataframe is:')
    df.printSchema()
    #print(f'The Dataframe is:{df.show()}')
    print('****************************************************************')
    print(f'The the dataframe is:')
    df.show()
    print('****************************************************************')

    # Retrieving the data from the dataframe using collect
    df_2=df.collect()
    print(f'The retrieved Data is:{df_2}')
    print('****************************************************************')

    # print 0th row and all the columns
    print('0th Row and all the columns:')
    print(df.collect()[0][0:])
    print('****************************************************************')
    print(f'No. Of records in the dataframe:{df.count()}')
    print('****************************************************************')

    # retrieving multiple rows using collect, count and for loop
    print(f'All the rows in the Dataframe:')
    for row in df.collect()[0:df.count()]:
        print((row["State"]),",",str(row["Cases"]),",",str(row["Recovered"]),",",str(row["Deaths"]))
    print('****************************************************************')
    # retrieving data of all the columns
    print('All the columns of the dataframe:')
    for column in df.collect():
        print(column["State"],",",column["Cases"], column["Recovered"], ",", column["Deaths"])
    print('****************************************************************')
    # Print the columns of the dataframe with the col function
    # print(df.select(col("State")).show())
    df.select(col("State"),col("Cases"),col('Recovered'), col("Deaths")).show()

    data = [
        ("James", 'Smith', 'USA', 'CA'),
        ("Michael", 'Rose', 'USA', 'NY'),
        ("Robert", 'Williams', 'USA', 'CA'),
        ("Maria", 'Jones', 'USA', 'FL'),
    ]
    columns = ["firstname", "lastname", "country", "state"]
    df_1 = spark.createDataFrame(data, schema=columns)
    # df_1.show()
    # df_1.select(col("State"),col("country")).show()
    # print(df_1.select(col("firstname"), col("lastname")).show())