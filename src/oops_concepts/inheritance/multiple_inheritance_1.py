# Python example to show the working of multiple
# inheritance

class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")

    def show_country(self):
        """
        Displaying the country
        Returns:

        """
        print("I stay in India")


class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")

    def show_employer(self):
        """
        Display Employer
        Returns:

        """
        print("I work for Abzooba")


class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def print_strs(self):
        print(self.str1, self.str2)


# Driver code
if __name__=="__main__":
    child = Derived()
    child.print_strs()
    # Call Base 1 Method
    child.show_country()

    # Call Base 2 Method
    child.show_employer()
