print('''Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie''')

dzialanie = int(input("Wpisz numer operacji: "))
arg1 = float(input('Podaj argument 1: '))
arg2 = float(input('Podaj argument 2: '))

if dzialanie == 1:
    w = arg1 + arg2
elif dzialanie == 2:
    w = arg1 - arg2
elif dzialanie == 3:
    w = arg1 * arg2
elif dzialanie == 4:
    w = arg1 / arg2
elif dzialanie == 5:
    w = arg1 ** arg2

print(f'Wynik = {w}')
