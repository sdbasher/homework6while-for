number = int(input('Введіть ціле додатне чісло: '))

total = 0
result = 1

while result <= number:
    if result % 3 != 0:
        total += result ** 3
    result += 1
print("Сума кубів всіх натуральних чисел від 1 до", number, "з урахуванням винятків :", total)







