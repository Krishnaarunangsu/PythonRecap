# python program to illustrate functions can be passed as arguments to other functions
def shout(text):
    """

    Args:
        text:

    Returns:

    """
    return text.upper()

def whisper(text):
    """

    Args:
        text:

    Returns:

    """
    return text.lower()

def greet(func):
    """
    Storing the function in a variable
    Args:
        func:

    Returns:

    """
    greeting=func("""Hi, I am created by a function passed as an argument""")
    print(greeting)

greet(shout)
greet(whisper)
