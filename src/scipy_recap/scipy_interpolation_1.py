# What is Interpolation? Interpolation is a method for generating points between given points. For example: for
# points 1 and 2, we may interpolate and find points 1.33 and 1.66. Interpolation has many usages:
# In Machine Learning, we often deal with missing data in a dataset,
# interpolation is often used to substitute those values.
# This method of filling values is called imputation. Apart from imputation,
# interpolation is often used where we need to smooth the discrete points in a dataset.

# 1D Interpolation
# The function interp1d() is used to interpolate a distribution with 1 variable.
# It takes x and y points and returns a callable function that can be called with new x and returns corresponding y.


# For given xs and ys interpolate values from 2.1, 2.2... to 2.9:
from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2 * xs + 1

interp_func = interp1d(xs, ys)
arr_2 = interp_func(np.arange(2.1, 3, 0.1))

print(f'Interpolation 1D:{arr_2}')

# Note: that new xs should be in same range as of the old xs, meaning that we cannot call interp_func() with values
# higher than 10, or less than 0.
