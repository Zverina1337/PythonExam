# Дан одномерный массив числовых значений, насчитывающий N элементов. Определить имеются ли в массиве два подряд идущих нуля.

from random import randint
n = int(input('N = '))

array = [randint(0, 2) for i in range(n)]
i = 0
flag = False
while i < len(array):
    if i + 1 < len(array):
        print(str(array[i]) + " : " + str(array[i + 1]))
        if array[i] == 0 and array[i + 1] == 0:
            flag = True
    i += 1

if flag:
    print('Имеются')
else:
    print('Не имеются')
print(array)