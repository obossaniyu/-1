import re

text = input("Введите строку: ")

words = re.findall(r"[a-zA-Zа-яА-ЯёЁ]+", text)

if len(words) == 0:
    print("В строке нет слов.")
else:
    count = len(words)

    longest = max(words, key=len)
    shortest = min(words, key=len)

    print("Количество слов:", count)
    print("Самое длинное слово:", longest)
    print("Самое короткое слово:", shortest)
