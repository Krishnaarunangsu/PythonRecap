# Inner Function
def parent():
    print('Printing from parent')

    def first_child():
        print("Printing from first_child()")

    def second_child():
        print("Printing from second_child()")

    first_child()
    second_child()

parent()