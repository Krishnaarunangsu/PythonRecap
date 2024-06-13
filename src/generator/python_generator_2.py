# A python program to demonstrate the use of generator object with next()
def simple_generator_function():
    """

    Returns:

    """
    yield 1
    yield 2
    yield 3

# x is a generator object
x=simple_generator_function()

# Iterating over the generator object using next
#In python 3 __next__()
print(f'The Value is:{next(x)}')
print(f'The Value is:{next(x)}')
print(f'The Value is:{next(x)}')
