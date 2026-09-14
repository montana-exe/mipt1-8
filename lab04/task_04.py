from functools import reduce

n = int(input("Введите число: "))
factorial = reduce(lambda result, number: result * number, range(1, n + 1), 1)

print(f"{n}! = {factorial}")
