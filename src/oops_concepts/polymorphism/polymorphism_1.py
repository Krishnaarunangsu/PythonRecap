class Bird:
    def intro(self):
        print("From Bird-There are many types of birds.")

    def flight(self):
        print("From Bird-Most of the birds can fly but some cannot.")


class Sparrow(Bird):
    def flight(self,name:str):
        print("Sparrows can fly.")
        print(f'Name of the Sparrow:{name}')


class Ostrich(Bird):
    def flight(self,country:str):
        print("Ostriches cannot fly.")
        print(f'Country of the Ostrich:{country}')


obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

obj_bird.intro()
obj_bird.flight()
print('*******************************************')

obj_spr.intro()
obj_spr.flight('Sparrow-1')
print('*******************************************')

obj_ost.intro()
obj_ost.flight('Australia')