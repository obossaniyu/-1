numbers = []

for i in range(10):
    num = float(input(f"Введите число {i + 1}: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

min_value = min(numbers)
max_value = max(numbers)

min_index = numbers.index(min_value)
max_index = numbers.index(max_value)

print("\nМассив:", numbers)
print("Сумма элементов:", total)
print("Среднее арифметическое:", average)
print("Минимальное число:", min_value)
print("Индекс минимального числа:", min_index)
print("Максимальное число:", max_value)
print("Индекс максимального числа:", max_index)
