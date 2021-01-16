class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Draw : {self.x}  {self.y}')


point1 = Point(5, 10)

point1.draw()


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello {self.name}'


peter = Person('Peter James')

print(peter.greet())
