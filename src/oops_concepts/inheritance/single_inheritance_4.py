# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name:str, id_no:int):
        self.name = name
        self.id_no = id_no

    def display(self):
        print(self.name)
        print(self.id_no)


# child class
class Employee(Person):
    def __init__(self, name:str, id_no:int, salary:float, post:str):
        #self.name=name
        #self.id_no=id_no
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, id_no)


# Driver code
if __name__=="__main__":
    # creation of an object variable or an instance
    emp = Employee('Rahul', 886012, 200000, "Intern")

    # calling a function of the class Person using its instance
    emp.display()
    print(emp.salary)
    print(emp.post)