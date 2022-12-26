# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Поменять местами элементы, стоящие на чётных и нечётных местах: А(1) с А(2), А (3) с А(4) …
from random import randint

n = int(input('N = '))
array = [randint(0,10) for i in range(n)]
i = 0
j = 1
temp = 0
print(array)

while i < n and j < n:
    if i % 2 == 0:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
    j += 1
    i += 1

print(array)