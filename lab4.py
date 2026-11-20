numbers = list(map(int, input("Введите числа через пробел: ").split()))
x = int(input("Какое число удалить: "))

print("Исходный массив:", numbers)

i = 0

while i < len(numbers):
    if numbers[i] == x:
        for j in range(i, len(numbers) - 1):
            numbers[j] = numbers[j + 1]

        numbers.pop()
    else:
        i += 1

print("Массив после удаления:", numbers)