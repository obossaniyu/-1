import re

# Ввод строки
text = input("Введите строку: ")

# Разбиение строки на слова без спецсимволов
words = re.findall(r"[a-zA-Zа-яА-ЯёЁ]+", text)

# Проверка наличия слов
if len(words) == 0:
    print("В строке нет слов.")
else:
    # Подсчёт количества слов
    count = len(words)

    # Поиск длинного и короткого слова
    longest = max(words, key=len)
    shortest = min(words, key=len)

    # Вывод результатов
    print("Количество слов:", count)
    print("Самое длинное слово:", longest)
    print("Самое короткое слово:", shortest)
