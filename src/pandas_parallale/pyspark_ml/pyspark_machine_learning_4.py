from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import HashingTF, Tokenizer
import os,sys
import pyspark
from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


spark = SparkSession.builder.appName('SparkTutorial').getOrCreate()
# Prepare training documents
training = spark.createDataFrame([
    (0, "a b c d e spark", 1.0),
    (1, "b d", 0.0),
    (2, "spark f g h", 1.0),
    (3, "hadoop mapreduce", 0.0)
], ["id", "text", "label"])

# Configure an ML pipeline
tokenizer = Tokenizer(inputCol="text", outputCol="words")
hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="features")
lr = LogisticRegression(maxIter=10, regParam=0.001)
#print(f'{lr.fitIntercept}')
pipeline = Pipeline(stages=[tokenizer, hashingTF, lr])
print(f'Max Iterations:{lr.getMaxIter()}')
# Fit the pipeline to training documents
model = pipeline.fit(training)


# Save the trained model
# model.save("C:/Downloads/model_spark")