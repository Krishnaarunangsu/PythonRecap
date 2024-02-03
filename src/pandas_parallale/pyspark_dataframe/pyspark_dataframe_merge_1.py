# Example 1: Combining two DataFrames with the same schema
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


    # Create Dataframe from data
    df1 = spark_sess.createDataFrame([(1, 'A'), (2, 'B')], ['id', 'value'])
    df2 = spark_sess.createDataFrame([(3, 'C'), (4, 'D')], ['id', 'value'])
    df3 = df1.union(df2)
    df3.show()