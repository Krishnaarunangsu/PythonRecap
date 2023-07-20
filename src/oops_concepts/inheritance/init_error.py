class A:
    def __init__(self, name='Rahul'):
        self.name = name


class B(A):
    """

    """

    def __init__(self, name, roll):
        self.roll = roll
        super().__init__(name)


# obj_1 = B(23)
obj_1 = B('Jack', 23)
obj_2 = A('Tom')
# object = B()
# print(object.name)
print(obj_1.roll)
print(obj_1.name)
print(obj_2.name)
