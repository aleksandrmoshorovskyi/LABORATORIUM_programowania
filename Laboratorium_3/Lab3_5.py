#
n = int(input("How many students in the class?: "))
i = 1
m = 0

while i <= n:
    m += int(input(f"mark{i} :"))
    i += 1

s = m/n
print("sredne = ", s)