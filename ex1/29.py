# Вводятся положительные числа. Определить сумму чисел, делящихся на положительное число В нацело. При вводе отрицательного числа закончить работу.

b = int(input('B = '))
sum = 0

print('Введите числа')
while True:
    num = int(input())

    if num < 0:
        break
    elif num % b == 0:
        sum += num

print('Сумма чисел: ' + str(sum))