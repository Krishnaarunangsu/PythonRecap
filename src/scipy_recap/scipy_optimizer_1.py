# Find the root of the equation: x+cos(x)
from scipy.optimize import root
from math import cos


# Function representing an equation
def eqn(x):
    """

    :param x:
    :return: The square root
    """
    return x + cos(x)


# SciPy's optimize.root function.
# This function takes two required arguments:
# fun - a function representing an equation.
# x0 - an initial guess for the root.
# The function returns an object with information regarding the solution.
# The actual solution is given under attribute x of the returned object:
my_root = root(eqn, 0)

print(f'The Square root is:"\n{my_root.x}')
print(my_root)

