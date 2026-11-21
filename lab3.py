for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()

num = input("\nВведите число: ")
summa = 0

for cifra in num:
    summa += int(cifra)

print("Сумма цифр:", summa)
