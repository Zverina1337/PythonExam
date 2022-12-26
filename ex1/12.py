# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Сумму элементов массива и количество положительных элементов поставить на первое и второе место.
from random import randint

n = int(input('N = '))
array = [randint(-10,10) for i in range(n)]
pos_count = 0
i = 0

while n > i:
    num = int(input())
    array.append(num)
    if num > 0:
        pos_count += 1
    i += 1

sum_array = sum(array)
array.insert(0, sum(array))
array.insert(1, pos_count)
print('Сумма элементов массива: ' + str(sum_array))
print('Количество положительных элементов: ' + str(pos_count)) 
print(array)