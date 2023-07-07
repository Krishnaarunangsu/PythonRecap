class DemoClassMain:
    demo_value = 3

    # constructor
    def __init__(self):
        # initializing instance variable
        self.num = 100

    # a method
    def read_number(self):
        print(self.num)
        print('********************************************************************')
        print(f'Class Variable Value from Instance Method:{self.demo_value}')


if __name__ == "__main__":
    # creating object of the class. This invokes constructor
    obj = DemoClassMain()
    print(f'Class Variable Value:{DemoClassMain.demo_value}')

    # Num is not a class variable.The following statement will return error
    print(f'Class Variable Value:{DemoClassMain.num}')
    print('********************************************************************')

    # calling the instance method using the object obj
    obj.read_number()
