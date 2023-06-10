class Person:

    def __init__(self, name, gender,age, profession):
        """
        Initialization of data members (instance variables)
        Args:
            name:
            gender:
            age:
            profession:
        """

        self.name = name
        self.gender = gender
        self.age = age
        self.profession = profession

    # Behavior (instance methods)
    def show_person_details(self):
        """

        Returns:

        """

        print(f'Name:{self.name}, Gender:{self.gender}, Age:{self.age}, Profession:{self.profession}')

    # Behavior (instance methods)
    def work(self):
        """

        Returns:

        """
        print(self.name, 'working as a', self.profession)

if __name__=="__main__":

    # Instance 1
    person_1=Person("John", "M", 27,'Engineer')

    # Show Details
    person_1.show_person_details()
    # print(f'Person-1 Details:{}')
