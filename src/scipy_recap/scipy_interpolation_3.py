# Interpolation with Radial Basis Function
# Radial basis function is a function that is defined corresponding to a fixed reference point.
# The Rbf() function also takes xs and ys as arguments and produces a callable function that can be called with new xs.

# Interpolate following xs and ys using rbf and find values for 2.1, 2.2 ... 2.9:
from scipy.interpolate import Rbf
import numpy as np

xs = np.arange(10)
ys = 2 * xs + np.sin(xs) + 1

interp_func = Rbf(xs, ys)
arr_2 = interp_func(np.arange(2.1, 3, 0.1))

print(f'Radial Basis Function:{arr_2}')
