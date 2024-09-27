# Pivot and Unpivot
import os,sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import count,avg

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark=SparkSession.builder.appName('PySpark-Dataframe Group By').getOrCreate()

# Data
dataset=[
(1, "Quality", 4),
    (1, "Service", 3),
    (2, "Quality", 5),
    (2, "Service", 4),
    (3, "Quality", 2),
    (3, "Service", 3),
    (1, "Quality", 5),
    (1, "Service", 4),
    (2, "Quality", 4),
    (2, "Service", 5),
    (3, "Quality", 3),
    (3, "Service", 2)
]

columns=["Customer_Id", "Feedback_Category", "Rating"]

# Create the Dataframme
df=spark.createDataFrame(dataset, schema=columns)
print(f'The Dataframe Schema is:\n')
df.printSchema()
print(f'The Dataframe is:\n')
# df.show(truncate=True)
df.show(truncate=False)

# Analyze each customer’s average rating for each feedback category-Group By Customer Id and Pivot Feedback category values into Columns
print(f'Record Count for Every Department in the dataset with aggregate and count')
pivoted_df = df.groupby("Customer_Id").pivot("Feedback_Category").agg(avg("Rating"))
pivoted_df.show()

pivoted_df = df.groupBy("Customer_ID").pivot("Feedback_Category").agg(avg("Rating"))
pivoted_df.show()

# Unpivot the data
unpivoted_df = pivoted_df.selectExpr("Customer_Id", "stack(2, 'Quality', Quality, 'Service', Service) as (Feedback_Category, Rating)")
unpivoted_df.show()

# unpivoted_df = pivoted_df.selectExpr("Customer_ID", "stack(2, 'Quality', Quality, 'Service', Service) as (Feedback_Category, Rating)")
# unpivoted_df.show()




