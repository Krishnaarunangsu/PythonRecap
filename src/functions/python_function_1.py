# python program to illustrate functions can be treated as objects
def shout(text):
    """

    Args:
        text:

    Returns:

    """
    return text.upper()


yell=shout
print(yell('Krishna'))