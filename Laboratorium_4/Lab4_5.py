import random

punkty = []

# for i in range(15):
#     p = random.uniform(0, 50)
#     p = round(p, 2)
#     punkty.append(p)
punkty = [round(random.uniform(0, 50), 0) for i in range(15)]

print(punkty)
print()
print(f"Mazimum = {max(punkty)}, minimum = {min(punkty)}")

s = float(input("Podaj liczbe: "))

if s in punkty:
    x = punkty.index(s)
    print("index - ", x)
else:
    print("Niema liczbe v liste")

sr = round(sum(punkty)/len(punkty))
print("sr =", sr)

upper = []
lower = []
for i in punkty:
    if i > sr:
        upper.append(i)
    elif i < sr:
        lower.append(i)
    else:
        print(i)
print()
print(upper)
print(lower)
print()
print(len(upper), len(lower))
