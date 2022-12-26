# Имеется коробка со сторонами: АхВхС. Определить пройдёт ли она в дверь с размерами МхК 

a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))
m = int(input('M = '))
k = int(input('K = '))

if  (a <= m and b <= k
    or a <= m and c <= k
    or b <= m and a <= k
    or b <= m and c <= k
    or c <= m and a <= k
    or c <= m and b <= k):
    print('Коробка может пройти через дверь')
else:
    print('Коробка не может пройти через дверь')
