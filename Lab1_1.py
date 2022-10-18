#a
x1 = input("podaj x dla a(x): ")
x1 = float(x1)

if x1 > 0:
    x1 *= 2
elif x1 == 0:
    x1 = 0
elif x1 < 0:
    x1 *= -3

print("a(x) = ", x1)

#b
x2 = input("podaj x dla b(x): ")
x2 = float(x2)

if x2 >= 1:
    x2 *= x2
elif x2 < 1:
    x2 = x2

print("b(x) = ", x2)

#c
x3 = input("podaj x dla c(x): ")
x3 = float(x3)

if x3 > 2:
    x3 += 2
elif x3 == 2:
    x3 = 8
elif x3 < 2:
    x3 -= 4

print("c(x) = ", x3)
