# generator expression
# a generator that yields items instead of returning a list
def first(n):
    """

    Args:
        n:

    Returns:

    """
    num=0
    while num <n:
        yield num
        num+=1

for i in first(10):
    print(f'The number is:{i}')