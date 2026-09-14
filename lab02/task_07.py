text = input("Введите строку: ").lower()
vowels = "аеёиоуыэюяaeiou"
count = 0

for character in text:
    if character in vowels:
        count += 1

print(f"Количество гласных: {count}")
