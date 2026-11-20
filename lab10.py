
import json


class Inventory:
    def __init__(self):
        self.products = {}

    def add(self, name, price, quantity):
        """Добавление товара."""
        if not name.strip():
            raise ValueError("Введите название товара")
        if name in self.products:
            raise ValueError("Товар уже существует")
        if price < 0 or quantity < 0:
            raise ValueError("Отрицательные значения недопустимы")

        self.products[name] = {
            "price": price,
            "quantity": quantity
        }

    def get(self, name):
        """Получение информации о товаре."""
        return self.products[name]

    def update(self, name, price, quantity):
        """Редактирование товара."""
        if name not in self.products:
            raise KeyError("Товар не найден")
        if price < 0 or quantity < 0:
            raise ValueError("Отрицательные значения недопустимы")

        self.products[name] = {
            "price": price,
            "quantity": quantity
        }

    def delete(self, name):
        """Удаление товара."""
        del self.products[name]

    def report(self):
        """Формирование отчёта."""
        quantity = sum(
            p["quantity"] for p in self.products.values()
        )
        cost = sum(
            p["price"] * p["quantity"]
            for p in self.products.values()
        )

        return len(self.products), quantity, cost

    def save(self, filename="products.json"):
        """Сохранение товаров в файл."""
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.products, file,
                      ensure_ascii=False, indent=4)

    def load(self, filename="products.json"):
        """Загрузка товаров из файла."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.products = json.load(file)
        except FileNotFoundError:
            self.products = {}


def main():
    inventory = Inventory()
    inventory.load()

    while True:
        print("\n1. Добавить товар")
        print("2. Показать товары")
        print("3. Редактировать товар")
        print("4. Удалить товар")
        print("5. Отчёт")
        print("0. Выход")

        choice = input("Ваш выбор: ")

        try:
            if choice == "1":
                name = input("Название: ")
                price = float(input("Цена: "))
                quantity = int(input("Количество: "))
                inventory.add(name, price, quantity)
                inventory.save()
                print("Товар добавлен!")

            elif choice == "2":
                if not inventory.products:
                    print("Список товаров пуст")

                for name, p in inventory.products.items():
                    print(f"{name}: {p['price']:.2f} руб., "
                          f"{p['quantity']} шт.")

            elif choice == "3":
                name = input("Название товара: ")
                price = float(input("Новая цена: "))
                quantity = int(input("Новое количество: "))
                inventory.update(name, price, quantity)
                inventory.save()
                print("Товар обновлён!")

            elif choice == "4":
                name = input("Название товара: ")
                inventory.delete(name)
                inventory.save()
                print("Товар удалён!")

            elif choice == "5":
                count, quantity, cost = inventory.report()
                print("Количество видов товаров:", count)
                print("Всего единиц товара:", quantity)
                print(f"Общая стоимость: {cost:.2f} руб.")

            elif choice == "0":
                inventory.save()
                print("Программа завершена")
                break

            else:
                print("Неверный выбор!")

        except (ValueError, KeyError, OSError) as error:
            print("Ошибка:", error)


if __name__ == "__main__":
    main()
