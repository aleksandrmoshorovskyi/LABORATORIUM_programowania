# Zadanie 2. Napisz funkcje oblicz(), która ma dwa parametry i oblicza ich sumę oraz różnicę. Ponadto zwraca
# jednocześnie jak wynik dodawania, tak i odejmowania.

def compute(arg1, arg2):
    sum = arg1 + arg2
    riz = arg1 - arg2
    return sum, riz

print(compute(1, 2))

zm1, zm2 = compute(2, 5)
print(f"suma = {zm1}, riz = {zm2}")
