# Normality Tests (Skewness and Kurtosis)
# Normality tests are based on the skewness and kurtosis.
# The normaltest() function returns p value for the null hypothesis:
# "x comes from a normal distribution".
# Skewness:
# A measure of symmetry in data.
# For normal distributions it is 0.
# If it is negative, it means the data is skewed left.
# If it is positive it means the data is skewed right.
# Kurtosis:
# A measure of whether the data is heavy or lightly tailed to a normal distribution.
#
# Positive kurtosis means heavy tailed.
# Negative kurtosis means lightly tailed.

# Find skewness and kurtosis of values in an array:
import numpy as np
from scipy.stats import skew, kurtosis

v = np.random.normal(size=100)

skew_1 = skew(v)
kurt_1 = kurtosis(v)
print(f'Skewness:{skew_1}')
print(f'Kurtosis:{kurt_1}')

