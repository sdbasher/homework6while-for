number = int(input('Введіть ціле додатне чісло: '))

total = 0
for x in range(1, number + 1):
    if x % 3 != 0:
        total += x ** 3
print("Сума кубів всіх натуральних чисел від 1 до", number, "з урахуванням винятків :", total)