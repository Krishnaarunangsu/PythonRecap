# python program to illustrate functions
# Function can return another function
def create_adder(x:int):
    """

    Args:
        x:

    Returns:

    """
    def adder(y:int):
        """

        Args:
            y:

        Returns:

        """
        return x+y
    return adder

add_15=create_adder(15)
sum=add_15(10)
print(f'The Sum is:{sum}')