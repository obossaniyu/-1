n = int(input("Введите натуральное число: "))

if n <= 0:
    print("Ошибка! Число должно быть положительным")
else:
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    print("Делители числа:", *divisors)

    if sum(divisors) - n == n:
        print("Число является совершенным")
    else:
        print("Число не является совершенным")