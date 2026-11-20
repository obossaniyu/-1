
import math


def show_menu():
    """Вывод меню."""
    print("\nВыберите фигуру:")
    print("1. Круг")
    print("2. Треугольник")
    print("3. Прямоугольник")
    print("0. Выход")


def input_number(message):
    """Ввод числовых данных."""
    return float(input(message))


def circle_area(r):
    """Вычисление площади круга."""
    return math.pi * r ** 2


def triangle_area(a, h):
    """Вычисление площади треугольника."""
    return a * h / 2


def rectangle_area(a, b):
    """Вычисление площади прямоугольника."""
    return a * b


def show_result(area):
    """Вывод результата вычислений."""
    print(f"Площадь фигуры: {area:.2f}")


def main():
    """Основная функция программы."""
    while True:
        show_menu()
        choice = input("Ваш выбор: ")

        if choice == "1":
            r = input_number("Введите радиус: ")
            show_result(circle_area(r))

        elif choice == "2":
            a = input_number("Введите основание: ")
            h = input_number("Введите высоту: ")
            show_result(triangle_area(a, h))

        elif choice == "3":
            a = input_number("Введите сторону a: ")
            b = input_number("Введите сторону b: ")
            show_result(rectangle_area(a, b))

        elif choice == "0":
            print("Программа завершена.")
            break

        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()
