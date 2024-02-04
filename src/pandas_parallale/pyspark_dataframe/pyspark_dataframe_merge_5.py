# Example: Add missing columns to both the dataframes
from pprint import pprint

import pyspark.sql
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import SparkSession
import os,sys
import json

from pyspark.sql.types import StringType

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Create Spark Session
def create_spark_session():
    """
    Create a Spark Session
    Returns:
        spark_session

    """
    spark_session=SparkSession.builder.appName("Spark JSON Tutorial").getOrCreate()
    return spark_session

# Define the pyspark dataframe schema
def create_dataframe_schema():
    """
    Create dataframe schema
    Returns:
        dataframe_schema

    """
    dataframe_schema=StructType(
        [
          StructField("name", StringType()),
          StructField("age", IntegerType()),
          StructField("city", StringType())
         ]
    )
    return dataframe_schema

# Create Dataframe
def create_dataframe(spark_session:SparkSession,data:list, dataframe_schema:StructType)->pyspark.sql.DataFrame:
    """

    Args:
        spark_session:
        data:
        dataframe_schema:

    Returns:

    """
    # # Create a PySpark DataFrame
    df=spark_session.createDataFrame(data, dataframe_schema)
    return df

# Create JSON from Dataframe
def create_dataframe_json(df:pyspark.sql.DataFrame)->json:
    """

    Args:
        df:

    Returns:

    """
    # # Convert the PySpark DataFrame to a JSON string
    df_json=df.toJSON().collect()[0]
    print(str(df_json))

    with open("example1.json", "w") as f:
         # f.write(str(df_json))
         f.write(df_json)

    return json.loads(df_json)

if __name__=="__main__":
    # Create Spark Session
    spark_sess=create_spark_session()

    # Create Dataframe Schema
    df_schema=create_dataframe_schema()

    # Create Dataframe from data
    # list  of employee data
    data = [
            ["1", "sravan", "kakumanu"],
            ["2", "ojaswi", "hyd"],
            ["3", "rohith", "delhi"],
            ["4", "sridevi", "kakumanu"],
            ["5", "bobby", "guntur"]
    ]

    # specify column names
    columns = ['ID', 'NAME', 'Address']

    # creating a dataframe from the lists of data
    dataframe1 = spark_sess.createDataFrame(data, columns)

    # list  of employee data
    data = [
            ["1", 23],
            ["2", 21],
            ["3", 32],
        ]

    # specify column names
    columns = ['ID', 'Age']

    # creating a dataframe from the lists of data
    dataframe2 = spark_sess.createDataFrame(data, columns)

    for column in [column for column in dataframe2.columns
                   if column not in dataframe1.columns]:
        dataframe1=dataframe1.withColumn(column,lit(None))

    dataframe1.show()

    for column in [column for column in dataframe1.columns
                   if column not in dataframe2.columns]:
        dataframe2=dataframe2.withColumn(column,lit(None))

    dataframe2.show()

    # perform union. Union can only be performed on tables with the same number of columns
    # Can we union() DataFrames that have different schemas?
    # The union() can be performed on the DataFrames that have the same schema and structure.
    # If the schemas are different we may need to use unionByName() or make changes to
    # the DataFrames to align to their schemas before performing union() transformation.
    dataframe1.unionByName(dataframe2).show()