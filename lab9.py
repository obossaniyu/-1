
try:
    numbers = list(map(float, input(
        "Введите числа через пробел: "
    ).split()))

    if not numbers:
        raise ValueError("Массив не должен быть пустым")

    with open("numbers.txt", "w", encoding="utf-8") as file:
        for number in numbers:
            file.write(str(number) + "\n")

    print("Массив записан в файл numbers.txt")

    with open("numbers.txt", "r", encoding="utf-8") as file:
        data = [float(line.strip()) for line in file]

    total = sum(data)
    average = total / len(data)

    print("Массив из файла:", data)
    print("Сумма:", total)
    print("Среднее арифметическое:", average)

except FileNotFoundError:
    print("Ошибка: файл не найден!")

except ValueError:
    print("Ошибка: введите корректные числа!")

except PermissionError:
    print("Ошибка: нет доступа к файлу!")

except ZeroDivisionError:
    print("Ошибка: файл не содержит чисел!")

except OSError as error:
    print("Ошибка работы с файлом:", error)
