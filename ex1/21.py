# Даны действительные положительные числа а, b, с, d.
# Выясните, может ли прямоугольник со сторонами a,b  уместиться внутри прямоугольника со сторонами c,d  так,
# чтобы каждая сторона внутреннего прямоугольника была параллельна или перпендикулярна стороне внешнего прямоугольника.

import random

a = random.randint(1,100)
print("a= " + str(a))

b = random.randint(1,100)
print("b= " + str(b))

c = random.randint(1,100)
print("c= " + str(c))

d = random.randint(1,100)
print("d= " + str(d))

if (a <= c and b <= d) or (a <= d and b <= c):
    print(f"Данный прямоугольник со сторонами {a}:{b} может уместиться в прямоугольнике со сторонами {c}:{d}")
else:
    print(f"Данный прямоугольник со сторонами {a}:{b} не может уместиться в прямоугольнике со сторонами {c}:{d}")
