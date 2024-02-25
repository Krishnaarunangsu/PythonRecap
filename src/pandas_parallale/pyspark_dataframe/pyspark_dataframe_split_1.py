# Example 1: Combining two DataFrames with the same schema
from pprint import pprint

import pyspark.sql
from pyspark.sql import DataFrame
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
           StructField("BRAND", StringType()),
           StructField("PRODUCT", StringType())
          ]
     )
    # dataframe_schema=["BRAND","PRODUCT"]
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

#  Split dataframe using ‘DataFrame.limit()’
def split_dataframe(split_count, dataset:DataFrame):
    """

    Args:
        split_count:
        dataset (object):

    Returns:

    """
    # Calculate count of each dataframe rows
    each_len = dataset.count()
    print(f'Dataframe Rows:{each_len}')
    copy_df=dataset

    #temp_df = copy_df.limit(each_len)
    #temp_df.show()
    # Iterate for each dataframe
    i = 0
    while i < split_count:
        # Get the top `each_len` number of rows
        temp_df = copy_df.limit(split_count)
        copy_df = copy_df.subtract(temp_df)
        #copy_df.show()
        # View the dataframe
        temp_df.show(truncate=False)

        # Increment the split number
        i += 1



if __name__=="__main__":
    # Create Spark Session
    spark_sess=create_spark_session()
    dataframe_columns=create_dataframe_schema()

    # Row data for the dataframe : list of Tuples
    dataset:list=[
    ("HP", "Laptop"),
    ("Lenovo", "Mouse"),
    ("Dell", "Keyboard"),
    ("Samsung", "Monitor"),
    ("MSI", "Graphics Card"),
    ("Asus", "Motherboard"),
    ("Gigabyte", "Motherboard"),
    ("Zebronics", "Cabinet"),
    ("Adata", "RAM"),
    ("Transcend", "SSD"),
    ("Kingston", "HDD"),
    ("Toshiba", "DVD Writer")
]
    df3:DataFrame=create_dataframe(spark_sess, dataset,dataframe_columns)
    #df3=spark_sess.createDataFrame(dataset,dataframe_columns)

    df3.show()

    split_dataframe(4,df3)