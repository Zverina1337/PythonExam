# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Добавить столько элементов, чтобы положительных и отрицательных стало бы поровну.
from random import randint

n = int(input('N = '))
array = [randint(-10,10) for i in range(n)]
i = 0
pos_count = 0
neg_count = 0
count = 0

while i < n:
    num = int(input())
    array.append(num)
    if num > 0:
        pos_count += 1
    else:
        neg_count += 1
    i += 1

if pos_count > neg_count:
    j = 0
    count = pos_count - neg_count
    print('Нужно ' + str(count) + " отрицательных чисел")

    while count > j:
        rand_num = randint(-10, -1);
        array.append(rand_num)
        j += 1
elif neg_count > pos_count:
    j = 0
    count = neg_count - pos_count
    print('Нужно ' + str(count) + " положительных чисел")

    while count > j:
        rand_num = randint(1, 10);
        array.append(rand_num)
        j += 1
else:
    print('Кол-во положительных и отрицательных чисел равны')

print(array)