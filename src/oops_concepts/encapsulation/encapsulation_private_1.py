# Python program to demonstrate private members
# Creating a Base class


class Base:
    def __init__(self):
        """
         Initialization
        """
        self.a = "Geeks for Geeks"
        self.__c = "Again Geeks for Geeks"

    def display_private_member_from_base_class(self):
        """

        Returns:

        """
        print(f'Base Class-Private Member of the base class:{self.__c}')


# Creating a derived class
class Derived(Base):
    def __init__(self):
        """
        Initialization
        """
        # Calling constructor of Base class
        self.d = 10
        # print(f'Derived Class member:{self.d}')
        Base.__init__(self)
        # print("Calling private member of base class from the derived class: ")
        # print(f'{self.__c}')

    def display_private_member_from_derived_class(self):
        """

        Returns:

        """
        print(f'Derived Class-Public Member:{self.d}')
        # print(f'Derived Class-Private Member of the base class:{self.__c}')


# Driver code
obj1 = Base()
print(f'Public member of the base class:{obj1.a}')

# Uncommenting print(obj1.c) will raise an AttributeError
# print(obj1.__c)
# print(obj1.c)

# Uncommenting obj2 = Derived() will also raise an AttributeError as
# private member of base class is called inside derived class
obj2 = Derived()
obj2.display_private_member_from_derived_class()
obj2.display_private_member_from_base_class()
