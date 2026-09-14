class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


first = Vector(1, 2)
second = Vector(3, 4)
result = first + second

print(f"{first} + {second} = {result}")
