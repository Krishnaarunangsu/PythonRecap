class Parrot:
    # Class Attribute
    species = 'bird'

    # Instance Attribute -  Constructor Concepts
    def __init__(self, name: str, age: int):
        """

        :param name:
        :param age:
        :return None
        """
        self.name = name
        self.age = age

    # Show the species
    @classmethod
    def show_species(cls):
        print(f'The species is:{cls.species}')

    # def show_species_1(self):
    #     print(f'The species in the instance is:{self.species}')

    # Without any arguments
    def show_parrot_details(self):
        print(f'Name of the bird is:{self.name}')
        print(f'Ge of the bird is:{self.age} years')

    def main(self):
        self.show_species()
        self.show_species_1()
        self.show_parrot_details()
        print('\n')


if __name__ == "__main__":
    parrot = Parrot('Jim', 10)
    parrot.main()

    parrot = Parrot('Jerry', 20)
    parrot.main()
