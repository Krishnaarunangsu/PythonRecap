# https://www.atatus.com/blog/class-variables-vs-instance-variables-in-java/#:~:text=Class%20variables%20are%20accessed%20using,followed%20by%20the%20variable%20name.&text=Class%20variables%20are%20useful%20for%20storing%20data%20that%20is%20shared,as%20constants%20or%20default%20values.
# https://pynative.com/python-class-variables/
class Employee:
    """
    Employee class to define an Employee
    """
    office_name="XYZ Private Limited"
    def __init__(self, employee_name:str, employee_id:str):
        """

        Args:
            employee_name: str
                   Name of the employee
            employee_id: str
                   Employee ID of the employee
        """
        self.employee_name=employee_name
        self.employee_id=employee_id


    def show_employee_details(self):
        """
        Shows employee details
        Returns:

        """
        print(f'Office Name:{Employee.office_name}')
        print(f'Office Name:{self.office_name}')
        print(f'Employee Name:{self.employee_name}')
        print(f'Employee Id:{self.employee_id}')

if __name__=="__main__":
    employee=Employee("Ram", "T0165")
    employee.show_employee_details()
    print('***********************Modifying the class variable****************************')
    # Modify class variable
    Employee.office_name = 'PQR Private Limited'
    employee.show_employee_details()

    employee_2 = Employee("Narayan", "S0165")
    employee_2.show_employee_details()