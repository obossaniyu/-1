def input_text():
    """Ввод строки."""
    return input("Введите строку: ")


def word_count(text):
    """Подсчёт количества слов."""
    return len(text.split())


def reverse(text):
    """Переворот строки."""
    return text[::-1]


def to_upper_first(text):
    """Перевод первой буквы каждого слова в верхний регистр."""
    return " ".join(word.capitalize() for word in text.split())


def is_palindrome(text):
    """Проверка строки на палиндром."""
    text = "".join(c.lower() for c in text if c.isalnum())
    return text == text[::-1]


def show_result(text):
    """Вывод результатов обработки строки."""
    print("Количество слов:", word_count(text))
    print("Обратная строка:", reverse(text))
    print("Первые буквы заглавные:", to_upper_first(text))

    if is_palindrome(text):
        print("Строка является палиндромом")
    else:
        print("Строка не является палиндромом")


def main():
    text = input_text()
    show_result(text)


if __name__ == "__main__":
    main()