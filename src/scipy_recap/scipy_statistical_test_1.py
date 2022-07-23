# T-Test T-tests are used to determine if there is significant deference between means of two variables. and lets us
# know if they belong to the same distribution. It is a two-tailed test. The function ttest_ind() takes two samples
# of same size and produces a tuple of t-statistic and p-value.

# Find if the given values v1 and v2 are from same distribution:
import numpy as np
from scipy.stats import ttest_ind

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)
p_value = res.pvalue

print(f'TTest:{res}')
print(f'p-value:{p_value}')
