
class Book:
    """Класс для хранения информации о книге."""

    def __init__(self, title, author, year, price):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__price = price

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    @property
    def price(self):
        return self.__price

    def discount(self, percent):
        if 0 <= percent <= 100:
            self.__price *= 1 - percent / 100
        else:
            print("Некорректная скидка!")

    def show_info(self):
        print("Название:", self.title)
        print("Автор:", self.author)
        print("Год издания:", self.year)
        print(f"Цена: {self.price:.2f} руб.")

    def compare(self, other):
        if self.price > other.price:
            print(self.title, "дороже")
        elif self.price < other.price:
            print(other.title, "дороже")
        else:
            print("Цены книг одинаковые")


def input_book():
    title = input("Введите название: ")
    author = input("Введите автора: ")
    year = int(input("Введите год издания: "))
    price = float(input("Введите цену: "))
    return Book(title, author, year, price)


print("Введите данные первой книги:")
book1 = input_book()

print("\nВведите данные второй книги:")
book2 = input_book()

percent = float(input("\nВведите скидку на первую книгу (%): "))
book1.discount(percent)

print("\nПервая книга:")
book1.show_info()

print("\nВторая книга:")
book2.show_info()

print("\nРезультат сравнения:")
book1.compare(book2)
