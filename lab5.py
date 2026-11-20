import re

text = input("Введите строку: ")

numbers = re.findall(r"-?\d+", text)
numbers = list(map(int, numbers))

if numbers:
    print("Найденные числа:", *numbers)
    print("Сумма чисел:", sum(numbers))
else:
    print("В строке нет чисел")
    print("Сумма чисел: 0")