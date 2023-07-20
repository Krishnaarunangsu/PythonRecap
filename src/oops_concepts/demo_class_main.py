class DemoClassMain:
    """
    Demo Class Main
    """
    # Class Level Variable
    demo_value = 3

    # constructor
    def __init__(self):
        """
        Non-parameterized Constructor
        """
        # initializing instance variable
        self.num = 100

    def __init__(self, data):
        """
        Parameterized Constructor
        """
        # initializing instance variable
        self.num = data

    # a method
    def read_number(self):
        print(self.num)
        print('********************************************************************')
        print(f'Class Variable Value from Instance Method:{self.demo_value}')


if __name__ == "__main__":
    # creating object of the class. This invokes constructor
    obj = DemoClassMain(23)
    print(f'Class Variable Value:{DemoClassMain.demo_value}')

    # Num is not a class variable.The following statement will return error
    #print(f'Class Variable Value:{DemoClassMain.num}')
    print('********************************************************************')

    # calling the instance method using the object obj
    obj.read_number()
