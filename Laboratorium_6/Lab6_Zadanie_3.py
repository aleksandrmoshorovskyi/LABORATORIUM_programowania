# Zadanie 3. Napisz funkcję o zmiennej liczbie parametrów, która wyświetla wartości parametrów na ekranie.
# Następnie zmodyfikuj funkcję tak, aby znajdowała i zwracała wartość maksymalną.
# Wskazówka: użyj parametru *args, który łączy wszystkie dodatkowe (nadmiarowe) argumenty
# pozycyjne, niebędące słowami kluczowymi podczas wywoływania funkcji, w krotkę.

def zad_3(*args):
    print(args)
    for i in args:
        print(i)
    print()

zad_3(3, 4, "str", 8.85, [5, 7, "str"])
zad_3("Hello", 89)

def maximum(*args):
    print(args)
    k = args[0]
    for i in args:
        if i > k:
            k = i
    return k

print(maximum(3, 5, 4))
print(maximum("str", "akfi", "hello"))
