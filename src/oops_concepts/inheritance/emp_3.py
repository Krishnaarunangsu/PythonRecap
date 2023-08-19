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
        print("Employee 3 class has been called")

    def display(self):
        print(self.name, self.id,self.age)

if __name__=="__main__":
    employee_details = Employee("Mayank", 103, 20)

    # calling child class function
    employee_details.display()

    # Calling child class function
    employee_details.print()