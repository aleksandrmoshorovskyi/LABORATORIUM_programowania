# Zadanie 4. Napisz funkcję o zmiennej liczbie parametrów nazwanych, która wyświetla ich wartości na ekranie.
# Jeśli wśród przekazanych argumentów jest argument end, to oddzielaj wyświetlane wartości przypisaną do end
# wartością. W przeciwnym przypadku przypisz do end znak końca stringu.
# Wskazówka: użyj parametru ** kwargs, który łączy wszystkie dodatkowe nazwane argumenty, określone
# podczas wywoływania funkcji, w słownik. Argument przekazany przez słowo kluczowe jest uważany za
# nadmiarowy, jeśli słowo kluczowe, przez które zostało przekazane, nie pasuje do żadnej z nazw
# parametrów w definicji funkcji.

def zad4(**kwargs):
    if "koniec" in kwargs:
        end = kwargs["koniec"]
    else:
        end = "\n"
    for i in kwargs:
        print(i, kwargs[i], end = end)

zad4(wiek = 24, imie = "Marek")
zad4(a = 2, b = 10, c = True, koniec = ", ")
