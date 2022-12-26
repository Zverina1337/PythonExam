# Даны число Р и число Н.
# Определить сумму чисел меньше Р, произведение чисел больше Н и количество чисел в диапазоне значений Р и Н.
# При вводе числа равного Р или Н, закончить работу.

p = int(input('P = '))
h = int(input('H = '))
sum_p = 0
multi_h = 1
array_p_h = []

print('Введите числа: ')

while True:
    num = int(input())
    if num == p or num == h:
        break;
    elif num < p:
        sum_p += num
    elif num > h:
        multi_h *= num
    else:
        array_p_h.append(num)

print('SUM_P: ' + str(sum_p))
print('multi_h: ' + str(multi_h))
print(array_p_h)
