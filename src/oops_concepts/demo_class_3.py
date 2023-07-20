class DemoClass:
    """
        Demo Class
    """
    # Class Level Variable
    num = 101

    # Parameterized constructor
    def __init__(self, data):
        # Instance Variable Assigning value of the parameter
        self.num = data

    # a method
    def read_number(self):
        """
        Read the Number
        """
        print(f'Value of instance variable:{self.num}')


# creating object of the class
# this will invoke parameterized constructor
obj = DemoClass(55)

# calling the instance method using the object obj
obj.read_number()

# creating another object of the class
obj2 = DemoClass(66)

# calling the instance method using the object obj
obj2.read_number()
