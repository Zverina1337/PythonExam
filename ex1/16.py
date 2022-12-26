# Имеются две ёмкости: кубическая с ребром А, цилиндрическая с высотой Н и радиусом основания R.
# Определить поместится ли жидкость объёма М в первую ёмкость, во вторую, в обе.

import random
import math

A = random.randint(1,10)
Cube = A**3
print("V Cube = " + str(Cube))

H = random.randint(1,10)
R = random.randint(1,10)
pi=math.pi
Cylinder=pi*R**2*H
print("V Cylinder = " + str(Cylinder))

M=random.randint(1,100)
print("V Woter = " + str(M))

if Cube >= M:
    print("Water will fit in to the cube,")
elif Cube == M:
    print("Water will fit in to the cylinder,")
elif Cylinder == M:
    if Cylinder >= M:
        print("Water will fit into the cube and cylinder.")
elif Cylinder < M:
    if Cube < M:
        print("Water will not fit into the cube and cylinder.")
    