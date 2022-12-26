# Дан одномерный массив числовых значений, насчитывающий N элементов. Исключить все нулевые элементы.
from random import randint

n = int(input('N = '))

array = [randint(0, 1) for i in range(n)]
array_copy = []
for num in array:
    if num != 0:
        array_copy.append(num)

print(f'До: {array}')
print(f'После: {array_copy}')
