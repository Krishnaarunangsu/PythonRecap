class Person(object):

    # Constructor
    def __init__(self, name):
        """
        Initialization of Person(Parent Class)
        Args:
            name:
        """
        self.name = name

    # To get name
    def get_name(self):
        return self.name

    # To check if this person is an employee
    def is_employee(self):
        """
        Deciding employee or not
        Returns:

        """
        print("In Parent Class: Person")
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
    """
    Employee Class Child Class of Person
    """

    # Here we return true
    def is_employee(self):
        """
        Deciding employee or not
        Returns:

        """
        print("In Child Class: Employee")
        return True


    # Driver code
if __name__=="__main__":

    emp = Person("Geek1")  # An Object of Person
    print(f'{emp.get_name()} and Employee Status:{emp.is_employee()}')
    print('***********************************************')

    emp = Employee("Geek2")  # An Object of Employee
    print(f'{emp.get_name()} and Employee Status:{emp.is_employee()}')
