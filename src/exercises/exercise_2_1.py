def factorial(n):
    """
    Calculate Factorial
    Args:
        n:

    Returns:

    """
    x=1
    if n != 0 and n != 1:
        while n > 1:
            x = x * n
            n = n - 1
    else:
        pass
    return x

list_1=[5,8,4, 7, 3, 0, 1, -3]
list_2=[]
list_2=[factorial(x) for  x in list_1 if x >=0]
print(f'The factorial for the list of numbers:{list_2}')


