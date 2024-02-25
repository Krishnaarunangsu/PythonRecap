def divide(num_1:int, num_2:int)->float:
    """Division of two integers and returns a float

    Args:
        num_1: int
                The divisor
        num_2: int
                The dividend

    Returns:
        quotient: float
                    The quotient of the above two numbers

    Raises:
        ValueError: Raises ValueError if the number(s) are not integer
        ZeroDivisionError: Raises ZeroDivisionError if the denominator is zero


    """
    if (not type(num_1) is int) or (not type(num_2) is int):
        raise ValueError('The number should be an integer')
    if num_2==0:
        raise ZeroDivisionError('The Denominator is zero')
    quotient=num_1/num_2
    return quotient

if __name__=="__main__":
    divide(3,0)