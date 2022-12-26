# Известна денежная сумма. Разменять её купюрами 500, 100, 10 и монетой 2 руб., если это возможно.

from random import randint

money = randint(1, 100000)
money_copy = money
banknote_500 = 0
banknote_100 = 0
banknote_10 = 0
banknote_2 = 0

if money % 2 == 0:
    print('Деньги можно разменять ' + str(money) + ' руб')

    while money_copy - 500 > 0:
        money_copy -= 500
        banknote_500 += 1

    while money_copy - 100 > 0:
        money_copy -= 100
        banknote_100 += 1

    while money_copy - 10 > 0:
        money_copy -= 10
        banknote_10 += 1

    while money_copy - 2 >= 0:
        money_copy -= 2
        banknote_2 += 1
    
    print(f'Из {money} руб. Получилось {banknote_500} купюр по 500 руб., {banknote_100} купюр по 100 рублей, {banknote_10} монет по 10 руб., {banknote_2} монет по 2 руб.')
else:
    print('Деньги нельзя разменять ' + str(money) + ' руб')