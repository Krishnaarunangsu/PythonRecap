# Python program to demonstrate protected members
# Creating a base class
class Base:
    def __init__(self):
        """
        Initialization
        """
        # Protected member
        self._a = 2


# Creating a derived class
class Derived(Base):
    def __init__(self):
        """
        Initialization
        """
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print(f'Calling protected member of base class: {self._a}')

        # Modify the protected variable:
        self._a = 3
        print(f'Calling modified protected member outside class: {self._a}')


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print(f'Accessing protected member of obj1 (from the derived class object): {obj1._a}')

# Accessing the protected variable outside
print(f'Accessing protected member of obj2 (from the base class object):{obj2._a}')