# Zadanie 2 (2.py) Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz średnie
# spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu paliwa oraz o szacowanych
# kosztach podróży (cena paliwa 6.5 zł/l).

droga = float(input('podai droge : '))
sredneSpalanie = float(input('podai średnie spalanie : '))

zlotych = (droga / 100) * sredneSpalanie
print('zużyciu paliwa', zlotych)
print('kosztach podróży', zlotych * 6.5, 'zl')
