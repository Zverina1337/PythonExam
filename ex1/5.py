# Заданы М строк слов, которые вводятся с клавиатуры. Подсчитать количество гласных букв в каждой из заданных строк.

string = input('Введите строку: ')
array = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
count = 0

for symbol in string:
    for gl_symbol in array:
        if symbol == gl_symbol:
            count += 1

print('Кол-во гласных букв: ' + str(count));