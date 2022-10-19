# 4
import random

x = random.randint(0, 99)
y = random.randint(0, 99)
z = random.randint(0, 99)

l1 = x
l2 = y
l3 = z

print('x =', x, 'y =', y, 'z =', z)

if l1 > l2:
    t = l1
    l1 = l2
    l2 = t

if l2 > l3:
    t = l2
    l2 = l3
    l3 = t

if l1 > l2:
    t = l1
    l1 = l2
    l2 = t

print('l1 =', l1, 'l2 =', l2, 'l3 =', l3)
