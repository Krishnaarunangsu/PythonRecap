# A Python program to demonstrate inheritance
# Base or Super class. Note object in bracket.(Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is equivalent to "class Person(object)"

class Base(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def get_name(self):
        return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):

    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    # To get name
    def get_age(self):
        return self.age


# Inherited or Sub class (Note Person in bracket)

class GrandChild(Child):

    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    # To get address
    def get_address(self):
        return self.address


# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(f'Name:{g.get_name()}, Age:{g.get_age()}, Address:{g.get_address()}')