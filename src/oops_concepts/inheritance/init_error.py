class A:
    def __init__(self, n='Rahul'):
        self.name = n


class B(A):
    """

    """
    def __init__(self, roll):
        self.roll = roll

object = B(23)
#object = B('Tom')
#object = B()
# print(object.name)
print(object.roll)