class DemoClass:
    """
    Demo C;ass
    """
    # Class Level Variable
    num = 101

    # non-parameterized constructor
    def __init__(self):
        """
        No-argument/default constructor
        """
        # Instance Variable
        self.num = 999

    # a method
    def read_number(self):
        print(f'Instance variable num:{self.num}')


# Print the class variable 'num'
print(f'Class Variable Value of num before Object Creation:{DemoClass.num}')
# creating object of the class
obj = DemoClass()

# calling the instance method using the object obj
obj.read_number()
# Print the class variable 'num'
print(f'Class Variable Value of num after Object Creation:{DemoClass.num}')
