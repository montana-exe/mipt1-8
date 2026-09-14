n = int(input("Введите N: "))
total = 0

for number in range(1, n + 1):
    if number % 2 != 0:
        total += number

print(f"Сумма нечётных чисел до {n}: {total}")
