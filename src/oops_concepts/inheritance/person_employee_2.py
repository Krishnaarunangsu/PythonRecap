# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):
    """
    Person: Parent Class
    """

    # __init__ is known as the constructor
    def __init__(self, name, id_number):
        """
        Initialization
        Args:
            name:
            id_number:
        """
        self.name = name
        self.id_number = id_number

    def display(self):
        """
        Display Person Details
        Returns:

        """
        print(f'Name:{self.name}')
        print(f'Id:{self.id_number}')


# child class
class Employee(Person):
    """
    Employee-Child/Sub-class of Person
    """
    def __init__(self, name, id_number, salary, post):
        """

        Args:
            name:
            id_number:
            salary:
            post:
        """
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, id_number)


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()