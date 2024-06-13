# Generator function for fibonacci numbers
def get_fibonacci_numbers(nums):
    """

    Args:
        nums:

    Returns:

    """
    x, y=0,1
    for _ in range(nums):
        print(f'X:{x}')
        print(f'Y:{y}')
        x, y=y, x+y
        yield x
# yield _

for i in get_fibonacci_numbers(10):
    print(i)