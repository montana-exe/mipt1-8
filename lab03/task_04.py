class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


shape = Shape(4, 5)
print(f"Площадь: {shape.area()}")
print(f"Периметр: {shape.perimeter()}")
