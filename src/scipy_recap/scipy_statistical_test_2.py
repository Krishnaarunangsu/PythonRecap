# KS-Test
# KS test is used to check if given values follow a distribution.
# The function takes the value to be tested, and the CDF as two parameters.
# A CDF can be either a string or a callable function that returns the probability.
# It can be used as a one tailed or two-tailed test.
# By default, it is two tailed. We can pass parameter alternative as a string of one of two-sided, less, or greater.

# Find if the given values v1 and v2 are from normal distribution:
import numpy as np
from scipy.stats import kstest

v = np.random.normal(size=100)

res = kstest(v, 'norm')
print(f'KS Test:{res}')

