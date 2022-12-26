# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Добавить к элементам массива такой новый элемент,
# чтобы сумма положительных элементов стала бы равна модулю суммы отрицательных элементов.
from random import randint

n = int(input('N = '))
array = [randint(0,10) for i in range(n)]
neg_sum = 0
pos_sum = 0
needed_num = 0
i = 1
print('Введите числа: \n')

while i < n:
    num = int(input())
    array.append(num)
    if num < 0:
        neg_sum += abs(num)
    else:
        pos_sum += num
    i += 1 

if neg_sum > pos_sum:
    needed_num = neg_sum - pos_sum
    array.append(needed_num)
    print('Нужно положительное число: ' + str(needed_num))
elif pos_sum > neg_sum:
    needed_num = pos_sum - neg_sum
    array.append(-needed_num)
    print('Нужно отрицательное число: ' + str(-needed_num))
else:
    print('Суммы уже равны')

print('Сумма положительных чисел: '+ str(pos_sum))
print('Сумма отрицательных чисел по модулю: '+ str(neg_sum))
print(array)