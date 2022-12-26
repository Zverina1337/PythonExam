# Заданы М строк символов, которые вводятся с клавиатуры. Найти количество символов в самой длинной строке.
# Выровнять строки по самой длинной строке, поставив перед каждой строкой соответствующее количество звёздочек.

m = int(input('M = '))
array_sizes = []
string = ''
i = 0
new_string = ''

while i < m:
    word = input()
    string += word + " "
    array_sizes.append(len(word))
    i += 1

array_sizes.sort()
max_count_symb = max(array_sizes)

for word in string.split(' ')[:-1]:
    if len(word) <= max_count_symb:
        count = max_count_symb - len(word)
        k = 0
        while k < count:
            word += "*"
            k += 1
    print(word)
    new_string += word + " "

print('Количество символов в самой длинной строке: ' + str(max_count_symb))
print('До: ' + string)
print('После: ' + new_string)