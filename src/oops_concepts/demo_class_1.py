class DemoClass:
    num = 101

    def __init__(self):
        """
        No argument Constructor
        """
        # does nothing.

    # a method
    def read_number(self):
        print(self.num)


# creating object of the class
obj = DemoClass()

# calling the instance method using the object obj
obj.read_number()