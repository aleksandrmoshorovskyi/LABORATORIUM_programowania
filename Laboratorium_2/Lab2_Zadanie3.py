# Zadanie 3 (3.py):
# • Dla osób poniżej 4 roku życia wstęp jest bezpłatny.
# • Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.
# • Dla osób powyżej 18 roku życia bilet kosztuje 20zł.
# Przykład: Wprowadź wiek klienta: 5
# Cena biletu: 10zł

# age = int(input("age klienta: "))
#
# if age < 4:
#     print("wstęp jest bezpłatny")
# elif age <= 18:
#     print("bilet kosztuje 10zł")
# else:
#     print("życia bilet kosztuje 20zł")

age = int(input("age klienta: "))
cena = 0

if age < 4:
    cena = 0
elif age <= 18:
    cena = 10
else:
    cena = 20

print(f"bilet kosztuje {cena}zł")
