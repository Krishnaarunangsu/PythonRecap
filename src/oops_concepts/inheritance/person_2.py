# A Python program to demonstrate inheritance
class Person(object):
    status="Good"

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def display(self):
        """
        Display Person details
        Returns:

        """
        print(self.name, self.id)


# Driver code
# per = Person("Satyam", 102)  # An Object of Person
# per.display()
# print(per.status)
