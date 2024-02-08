"""
Есть задача 
вычислить количество номеров
которые возможно получить по маске 000AAA00 - 999ZZZ20
"""
import string
import itertools

# Создаем список всех возможных букв
letters = list(string.ascii_uppercase)

# Создаем список всех возможных чисел для различных частей номера
numbers_001_999 = [str(i).zfill(3) for i in range(1, 1000)]
numbers_01_20 = [str(i).zfill(2) for i in range(1, 21)]

# Создаем все возможные комбинации для буквенной части номера
letter_combinations = [''.join(i) for i in itertools.product(letters, repeat=3)]

counter = 0
# Генерируем все возможные номера
for region in numbers_01_20:
    for letters in letter_combinations:
        for number in numbers_001_999:
            counter += 1

            print(counter, " : ", number + letters + region)


