# Step 1: Acquire the dataset
# Step 2: Import all the crucial libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import sklearn

# Step 3: Import the dataset
df=pd.read_csv("C://Arunangsu//Data//Datasets//Data.csv")
df.info()
print(f'Description:\n{df.describe()}')
print(f'Dataframe:\n{df}')

x=df.iloc[0, :-1].values
print(f'The feature columns are:\n{x}')