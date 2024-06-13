# Generator function for fibonacci numbers
def get_fibonacci_numbers(nums):
    """

    Args:
        nums:

    Returns:

    """
    x, y=0,1
    for _ in range(nums):
        x, y=y, x+y
        yield x


def square(nums):
    """

    Args:
        nums:

    Returns:

    """
    for num in nums:
        yield num**2

print(f'The sum of the square of the fibonacci numbers is:{sum(square(get_fibonacci_numbers(10)))}')