# Normality Tests (Skewness and Kurtosis)
# Normality tests are based on the skewness and kurtosis.
# The normaltest() function returns p value for the null hypothesis:
# "x comes from a normal distribution".

import numpy as np
from scipy.stats import normaltest

v = np.random.normal(size=100)
res= normaltest(v)

print(f'Normal Test:{res}')
