class Calculator:
    def add(self, first, second):
        return first + second

    def subtract(self, first, second):
        return first - second

    def multiply(self, first, second):
        return first * second

    def divide(self, first, second):
        if second == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return first / second


calculator = Calculator()

print(calculator.add(7, 3))
print(calculator.subtract(7, 3))
print(calculator.multiply(7, 3))
print(calculator.divide(7, 2))
