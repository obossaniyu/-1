class Employee:
    def __init__(self, name, position, salary, experience):
        self.__name = name
        self.__position = position
        self.__salary = salary
        self.__experience = experience

    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__position

    @property
    def salary(self):
        return self.__salary

    @property
    def experience(self):
        return self.__experience

    def bonus(self):
        if self.__experience >= 5:
            return self.__salary * 0.2
        else:
            return self.__salary * 0.1

    def tax(self):
        return (self.__salary + self.bonus()) * 0.13

    def total_salary(self):
        return self.__salary + self.bonus() - self.tax()

    def info(self):
        print("ФИО:", self.name)
        print("Должность:", self.position)
        print(f"Оклад: {self.salary:.2f} руб.")
        print("Стаж:", self.experience)
        print(f"Премия: {self.bonus():.2f} руб.")
        print(f"Налог: {self.tax():.2f} руб.")
        print(f"Итоговая зарплата: {self.total_salary():.2f} руб.")


def main():
    name = input("Введите ФИО: ")
    position = input("Введите должность: ")
    salary = float(input("Введите оклад: "))
    experience = int(input("Введите стаж: "))

    if salary < 0 or experience < 0:
        print("Ошибка! Отрицательные значения недопустимы")
        return

    employee = Employee(name, position, salary, experience)
    employee.info()


if __name__ == "__main__":
    main()