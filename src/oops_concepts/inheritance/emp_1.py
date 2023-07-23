from src.oops_concepts.inheritance.person_2 import Person


class Employee(Person):
    """

    """
    def __init__(self,name,id, age):
        """

        Args:
            name:
            id:
            age:
        """
        self.name=name
        self.id=id
        self.age=age


    def print(self):
        print("Employee class has been called")
        print('******************************************')
        print(f'The Age of the employee:{self.age}')



employee_details = Employee("Mayank", 103, 20)

# calling parent class function
employee_details.display()

# Calling child class function
employee_details.print()