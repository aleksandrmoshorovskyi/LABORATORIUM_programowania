import random
u = int(input("podaj lichbe: "))
b = []
for i in range(u):
    x = random.randint(1, 10)
    b.append(x)
print(b)
u = int(input("podaj lichbe: "))
#b_2 = []
#for i in range(u):
#    x = random.randint(5, 15)
#    b_2.append(x)
#print(b_2)

b_2 = [random.randint(5, 15) for i in range(u)]
print(b_2)

g = int(input("podaj lichbe: "))
if g in b:
    print("lizcbe z listu b")
elif g in b_2:
    print("lizcbe z listu b_2")
else:
    print("Nie ma takiej liczby w obu zestawach")

print()
b_3 = b + b_2
print(b_3)
b_3.sort()
print(b_3)
