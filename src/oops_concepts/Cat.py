class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self):
        """Find distance from origin"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @staticmethod
    def stat_meth():
        print("Look no self was passed")
        # print(self.x, self.y)


if __name__ == "__main__":
    p1 = Point(6, 8)
    distance_from_origin = p1.distance()
    print(f'Distance from the origin is:{distance_from_origin}')

    Point.stat_meth()
    p1.stat_meth()
