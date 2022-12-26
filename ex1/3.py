# Заданы М строк символов, которые вводятся с клавиатуры.
# Каждая строка представляет собой последовательность символов, включающих в себя вопросительные знаки.
# Заменить в каждой строке все имеющиеся вопросительные знаки звёздочками.

string = input('Введите строку: ')
array = string.split(' ')
new_string = ''

for word in array:
    word_without_que = ''

    for symbol in word:
        if symbol == '?':
            symbol = '*'

        word_without_que += symbol

    new_string += word_without_que + ' '


print(new_string)