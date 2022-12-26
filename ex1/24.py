# Дан одномерный массив числовых значений, насчитывающий N элементов. Вместо каждого нулевого элемента поставить сумму двух предыдущих элементов массива.

from random import randint

n = int(input('N = '))

array = [randint(0, 5) for i in range(n)]

print(array)
i = 0 
for num in array:
    if array[i] == 0 and i > 2:
        array[i] = array[i - 1] + array[i - 2]
    i += 1
print(array)
