# Суммировать вводимые числа, среди которых нет нулевых.
# При вводе нуля обеспечить вывод текущего значения суммы. При вводе числа 99999 закончить работу.

sum = 0
print('Введите числа')

while True:
    num = int(input())
    if num == 0:
        print('Сумма: ' + str(sum))
    elif num == 99999:
        break
    else:
        sum += num