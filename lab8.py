from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @abstractmethod
    def calculate(self):
        pass

    @abstractmethod
    def account_type(self):
        pass

    def info(self):
        print("Тип счёта:", self.account_type())
        print("Владелец:", self.owner)
        print(f"Баланс: {self.balance:.2f} руб.")
        print(f"Расчётный баланс: {self.calculate():.2f} руб.")
        print()


class Savings(Account):
    def calculate(self):
        return self.balance * 1.05

    def account_type(self):
        return "Сберегательный"


class Credit(Account):
    def calculate(self):
        return self.balance * 1.15

    def account_type(self):
        return "Кредитный"


class Salary(Account):
    def calculate(self):
        return self.balance

    def account_type(self):
        return "Зарплатный"


def main():
    accounts = [
        Savings("Иванов", 50000),
        Credit("Петров", -30000),
        Salary("Сидоров", 70000)
    ]

    for account in accounts:
        account.info()


if __name__ == "__main__":
    main()