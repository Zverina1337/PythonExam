# Заданы М строк символов, которые вводятся с клавиатуры. 
# Из заданных строк, каждая из которых представляет одно слово, составить одну длинную строку, разделяя слова пробелами.

print(' '.join([input() for i in range(int(input('m = ')))]))