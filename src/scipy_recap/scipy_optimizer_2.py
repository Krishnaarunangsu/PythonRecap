# Minimize the function x^2 + x + 2 with BFGS:
from scipy.optimize import minimize


# Function representing an equation
def eqn(x):
    """
    Minimizing an equation
    :param x:
    :return: The minimized object
    """
    return x ** 2 + x + 2


# SciPy's optimize.minimize function.
# This function takes three required arguments:
# fun - a function representing an equation.
# x0 - an initial guess for the root.
# method='BFGS'
# The function returns an object with information regarding the solution.
# The actual solution is given under attribute x of the returned object:
my_min = minimize(eqn, 0, method='BFGS')

print(f'The minimized value is:"\n{my_min}')
