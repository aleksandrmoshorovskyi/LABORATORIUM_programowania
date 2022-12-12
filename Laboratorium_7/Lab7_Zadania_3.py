import numpy as np

a = np.zeros((3, 3))
a[1:, :2] = 1
print(a)

b = np.zeros((3, 3))
b[:, 2:] = 1
print(b)

c = np.zeros((3, 3))
c[:2, :] = 1
print(c)

d = np.zeros((3, 3))
d[:2, 0] = 1
print(d)

e = np.zeros((3, 3))
e[:2, [0, 2]] = 1
# e[:2, 2] = 1
print(e)
