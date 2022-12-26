# Дан номер места в плацкартном вагоне. Определить, какое это место: верхнее или нижнее, в купе или боковое.

from random import randint

x = randint(1, 54)
string = 'Место в вагоне ' + str(x)
if x > 40:
    string += ' боковое,'
else:
    string += ' купе,'

if x % 2 == 0:
    string += ' верхнее.'
else:
    string += ' нижнее.'
    
print(string)