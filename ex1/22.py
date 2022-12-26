# Дан одномерный массив числовых значений, насчитывающий N элементов. Исключить из него М элементов, начиная с номера К.

from random import randint
n = int(input('N = '))
m = int(input('M = '))
k = int(input('K = '))

array = [randint(0, 10) for i in range(n)]
print(array)

del array[k:m+1]

print(array)