class Bird:
    """

    """

    def intro(self):
        """

        """
        print("From Bird-There are many types of birds.")

    def flight(self):
        print("From Bird-Most of the birds can fly but some cannot.")

    def flight(self, name: str):
        print("Sparrows can fly.")
        print(f'Name of the Bird:{name}')


obj_bird = Bird()

obj_bird.intro()
obj_bird.flight()
print('*******************************************')
obj_bird.flight('Shelly')
