first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))

first = abs(first)
second = abs(second)

while second != 0:
    remainder = first % second
    first = second
    second = remainder

print(f"НОД: {first}")
