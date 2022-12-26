# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Из элементов исходного массива построить два новых.
# В первый должны входить только положительные элементы, а во второй только отрицательные элементы.
from random import randint

n = int(input('N = '))
array = [randint(-10,10) for i in range(n)]
i = 0
pos_array = []
neg_array = []

while n > i:
    num = int(input())
    array.append(num)
    i += 1
for num in array:
    if num < 0:
        neg_array.append(num)
    else:
        pos_array.append(num)

print('Исходный массив: ' + str(array))
print('Массив положительных чисел: ' + str(pos_array))
print('Массив отрицательных чисел: ' + str(neg_array))
