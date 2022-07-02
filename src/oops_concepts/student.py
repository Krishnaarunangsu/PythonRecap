class Student:
    """
    Student class to define Student
    """
    school_name = "ABC School"

    # instantiation
    def __init__(self, student_name: str, student_age: int):
        """

        :param student_name:
        :param student_age:
        """
        self.student_name = student_name
        self.student_age = student_age

    @classmethod
    def change_school_name(cls, school_name: str):
        """

        :param school_name:
        :return:
        """
        cls.school_name = school_name

    def show_student_details(self):
        """

        :return:
        """

        print(f'School name is {self.school_name}')
        print(f'Student name is {self.student_name}')
        print(f'Student age is {self.student_age}')
        print('#########################################')

    def main(self):
        """

        :return:
        """
        self.show_student_details()


if __name__ == "__main__":
    student_1 = Student('John', 15)
    student_1.main()

    student_2 = Student('Eliza', 16)
    student_2.main()

    print('***********************')
    print('School name is changing')
    print('***********************')
    # Change the School name
    Student.change_school_name('XYZ School')
    student_1.main()
    student_2.main()
