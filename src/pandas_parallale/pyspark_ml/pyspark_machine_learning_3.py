from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
import pandas as pd
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
import six
# from pandas.plotting import scatter_matrix

sc = SparkContext()
sqlContext = SQLContext(sc)

# Loading Data
company_df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('Fortune 500 Companies US.csv')
print(company_df.take(1))

# Data Exploration
company_df.cache()
company_df.printSchema()

# Performing Descriptive Analysis
print(company_df.describe().toPandas().transpose())

# Finding the Correlation Between Independent Variables
numeric_features = [t[0] for t in company_df.dtypes if t[1] == 'int' or t[1] == 'double']
sampled_data = company_df.select(numeric_features).sample(False, 0.8).toPandas()
axs = pd.plotting.scatter_matrix(sampled_data, figsize=(10, 10))
n = len(sampled_data.columns)
for i in range(n):
    vertical = axs[i, 0]
    vertical.yaxis.label.set_rotation(0)
    vertical.yaxis.label.set_ha('right')
    vertical.set_yticks(())
    horizontal = axs[n-1, i]
    horizontal.xaxis.label.set_rotation(90)
    horizontal.set_xticks(())

#sampled_data.plot.scatter(x='length', y='width')

# Correlation Between Independent Variables
for i in company_df.columns:
    if not( isinstance(company_df.select(i).take(1)[0][0], six.string_types)):
        print( "Correlation to Employees for ", i, company_df.stat.corr('Number of Employees',i))


# Preparing Data
vectorAssembler = VectorAssembler(inputCols = ['Rank', 'Number of Employees'], outputCol = 'features')
t_company_df = vectorAssembler.transform(company_df)
t_company_df = t_company_df.select(['features', 'Number of Employees'])
t_company_df.show(3)

splits = t_company_df.randomSplit([0.7, 0.3])
train_df = splits[0]
test_df = splits[1]

# Linear Regression
lr = LinearRegression(featuresCol = 'features', labelCol='Number of Employees', maxIter=10, regParam=0.3, elasticNetParam=0.8)
lr_model = lr.fit(train_df)
print("Coefficients: " + str(lr_model.coefficients))
print("Intercept: " + str(lr_model.intercept))