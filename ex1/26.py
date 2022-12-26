# Определить сумму чисел с нечётными номерами и произведение чисел с чётными номерами.
# Подсчитать количество слагаемых и количество сомножителей. При вводе числа 55555 закончить работу.

sum_odd = 0
multi_even = 1
count_odd = 0
count_even = 0
print('Введите числа: ')
while True:
    num = int(input())
    if num == 55555:
        break;
    elif num % 2 == 0:
        count_even += 1
        multi_even *= num
    else:
        count_odd += 1
        sum_odd += num

print(f'Кол-во нечётных чисел: {count_odd}')
print(f'Сумма нечётных чисел: {sum_odd}')
print(f'Кол-во чётных чисел: {count_even}')
print(f'Произведение чётных чисел: {multi_even}')
