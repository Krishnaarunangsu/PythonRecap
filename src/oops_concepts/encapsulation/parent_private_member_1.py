# Python program to demonstrate private members
# of the parent class

class C(object):
    def __init__(self):
        self.c = 21 # Public
        self._f= 11 # Protected

        # d is private instance variable
        self.__d = 42 # Private


class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)

def show_details() -> object:
    """
    Global Function
    Returns:

    """
    print(C.c)
    print(C._f)

if __name__=="__main__":
    object1 = D()

    # produces an error as d is private instance variable
    print(object1.c)
    print(object1.e)
    print(object1._f)
    print(object1.__d)

    # Global Function
    show_details()
