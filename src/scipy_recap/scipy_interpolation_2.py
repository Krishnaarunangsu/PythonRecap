# Spline Interpolation In 1D interpolation the points are fitted for a single curve whereas in Spline interpolation
# the points are fitted against a piecewise function defined with polynomials called splines.
# The UnivariateSpline() function takes xs and ys and produce a callable function that can be called with new xs.
# Piecewise function: A function that has different definition for different ranges.

# Find univariate spline interpolation for 2.1, 2.2... 2.9 for the following non-linear points:
from scipy.interpolate import UnivariateSpline
import numpy as np

xs = np.arange(10)
ys = 2 * xs + np.sin(xs) + 1

interp_func = UnivariateSpline(xs, ys)
arr_2 = interp_func(np.arange(2.1, 3, 0.1))

print(f'Univariate Spline:{arr_2}')