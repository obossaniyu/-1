
try:
    # Ввод массива чисел
    numbers = list(map(float, input(
        "Введите числа через пробел: "
    ).split()))

    # Проверка пустого массива
    if not numbers:
        raise ValueError("Массив не должен быть пустым")

    # Запись массива в файл
    with open("numbers.txt", "w", encoding="utf-8") as file:
        for number in numbers:
            file.write(str(number) + "\n")

    print("Массив записан в файл numbers.txt")

    # Чтение массива из файла
    with open("numbers.txt", "r", encoding="utf-8") as file:
        data = [float(line.strip()) for line in file]

    # Вычисления
    total = sum(data)
    average = total / len(data)

    # Вывод результатов
    print("Массив из файла:", data)
    print("Сумма:", total)
    print("Среднее арифметическое:", average)

# Обработка исключений
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
