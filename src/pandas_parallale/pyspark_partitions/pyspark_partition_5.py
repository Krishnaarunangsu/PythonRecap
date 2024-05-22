# Range Partition
import pyspark, os, sys
from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.appName('answer').getOrCreate()

# Create Sample Dataframe
df=spark.createDataFrame([
    (1, "Alice", 25),
    (2, "Bob", 30),
    (3, "Charlie", 35),
    (4, "Dave", 40),
    (5, "Eve", 45),
    (6, "Frank", 50)
], ['id','name','age'])

# Print the dataframe
df.show()

# Perform Range Partition o the dataframe
# based on the "age" column
num_of_partitions=3
df=df.repartitionByRange(num_of_partitions,"age")

#Print the elements in each partition
lst=df.rdd.glom().collect()
print()
print(f'Each Partition:{df.rdd.glom().collect()}')

# printing the list using * and sep operator
print("printing lists separated by commas")

#print(*lst, sep = ", ")

# print in new line
print("printing lists in new line")

print(*lst, sep = "\n")

# printing the list using loop
for x in range(len(lst)):
    print('*******************************************')
    print(f'{x}:{lst[x]}')

