# 3
import math

a = input("podaj a dla ax2 + bx + c = 0 : ")
a: float = float(a)

b = input("podaj b dla ax2 + bx + c = 0 : ")
b: float = float(b)

c = input("podaj c dla ax2 + bx + c = 0 : ")
c: float = float(c)

if a == 0:
    print('error a =', a, '(a = 0)')
    exit()

D = b**2 - 4 * a * c

if D > 0:
    D_sqrt = math.sqrt(D)
    print(D_sqrt)

    x1 = (-b + D_sqrt) / (2 * a)
    x2 = (-b - D_sqrt) / (2 * a)

    print('x1 =', x1, 'x2 =', x2)
elif D == 0:
    x = -1*b / 2 * a

    print('x =', x)
elif D < 0:
    print('error D =', D, '(D < 0)')
