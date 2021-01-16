class Polygon:
    def __init__(self, no_of_sides):
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [int(input(f'Enter length of Side {i + 1} : ')) for i in range(len(self.sides))]

    def display_sides(self):
        for i in range(len(self.sides)):
            print(f'Side {i + 1} is {self.sides[i]}')


class Triangle(Polygon):
    pass


class Square(Polygon):
    def area(self):
        return self.sides[0] ** 2


triangle_a = Triangle(3)
triangle_a.input_sides()
triangle_a.display_sides()

square_a = Square(1)
square_a.input_sides()
square_a.display_sides()
print(square_a.area())
