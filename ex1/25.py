# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Подсчитать количество чисел, делящихся на 3 нацело, и среднее арифметическое чётных чисел.
# Поставить полученные значения на первое и последнее места в массиве (увеличив массив на 2 элемента).

from random import randint

n = int(input('N = '))
array = [randint(0,10) for i in range(n)]
average = 0
count_odd = 0
count_even = 0
sum_even = 0

for num in array:
    if num / 3 == 0:
        count_odd += 1
    
    if num % 2 == 0:
        count_even += 1
        sum_even += num

average = sum_even / count_even

print(array)
print('Среднее арифметическое: ' + str(average))
print('Кол-во чисел делящихся на 3 нацело: ' + str(count_odd))