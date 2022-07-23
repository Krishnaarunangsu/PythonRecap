# statistical Description of Data
# In order to see a summary of values in an array, we can use the describe() function.
# It returns the following description:
# number of observations (nobs)
# minimum and maximum values = minmax
# mean
# variance
# skewness
# kurtosis
import numpy as np
from scipy.stats import describe

v = np.random.normal(size=100)

res = describe(v)
print(f'Statistical Distribution:{res}')

