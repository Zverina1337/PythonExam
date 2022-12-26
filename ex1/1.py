# Для вводимых чисел определить процент положительных и отрицательных чисел. При вводе числа –65432 закончить работу.

array = []
pos_num = 0
neg_num = 0

while True:
    num = int(input('Введите число:'))

    if num == 65432:
        print("Массив:" + array)
        print('Процент отрицательных чисел в массиве: ' + str(round(100 / len(array) * neg_num)) + "%")
        print('Процент положительных чисел в массиве: ' + str(round(100 / len(array) * pos_num)) + "%")
        break;
    else:
        array.append(num)
        if num > 0:
            pos_num += 1
        elif num < 0:
            neg_num += 1