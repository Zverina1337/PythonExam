# Дан одномерный массив числовых значений, насчитывающий N элементов. Исключить из массива элементы, принадлежащие промежутку [В;С].
from random import randint

n = int(input('N = '))
b = int(input('B = '))
c = int(input('C = '))

array = [randint(0,10) for i in range(n)]

del array[b:c]
print(array)