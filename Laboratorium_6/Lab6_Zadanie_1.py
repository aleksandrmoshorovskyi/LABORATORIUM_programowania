# Zadanie 1.
# • Napisz funkcję o dwóch parametrach, imię oraz wiek, która wypisze ich wartości na ekranie.
# • Dodaj w następnej linii po nagłówku funkcji komentarz opisujący działanie funkcji. Wyświetl ten opis za
# pomocą instrukcji
# print(nazwa_funkcji.__doc__)
# • Jeśli w wywołaniu funkcji nie podano wieku, przypisz do parametru wiek wartość domyślną 20.
# Uwaga: Parametry z wartościami domyślnymi powinny być definiowane jako ostatnie na liście
# parametrów, ponieważ Python dopasowuje argumenty do parametrów na podstawie ich pozycji:
# def fun(param1, param2=default2, param3=default3)

def zad1(imie, wiek=22):
    print(imie, wiek)

zad1("Marek", 19)
zad1("Magda", 24)

zad1(wiek=30, imie="Andgej")

zad1("Kasia")
print(zad1("Kasia"))
