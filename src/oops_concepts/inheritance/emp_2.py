from src.oops_concepts.inheritance.person_2 import Person


class Employee(Person):
    """

    """

    def print(self):
        print("Employee class has been called")


if __name__=="__main__":
    # employee_details = Employee("Mayank", 103, 20)
    employee_details = Employee("Mayank", 103)

    # calling parent class function
    employee_details.display()

   # Calling child class function
    employee_details.print()