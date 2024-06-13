# A simple generator for Fibonacci Numbers
def fib(limit:int):
    """
    Generate Fibonacci numbers
    Returns:

    """
    #Initialize the first two numbers
    a, b=0, 1
    #Generate Fibonacci numbers one by one till the limit specified
    while a<limit:
        yield a
        a, b=b, a+b

# Create a generator object
x=fib(5)
print(f'The fibonacci number is:{next(x)}')
print(f'The fibonacci number is:{next(x)}')
print(f'The fibonacci number is:{next(x)}')
print(f'The fibonacci number is:{next(x)}')
print(f'The fibonacci number is:{next(x)}')

# Iterating the generator object using for loop
print(f'Using the for loop')
for i in fib(5):
    print(f'The fibonacci number is:"{i}')
