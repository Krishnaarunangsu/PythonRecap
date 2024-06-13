# A generator function that yields 1 for the first time, 2 second time and 3 third time
def simple_generator_function():
    """
    Generator function
    Returns:

    """
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
for value in simple_generator_function():
    print(f'The Value is:{value}')