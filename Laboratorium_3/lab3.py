w = int(input('podaj liczbe 1: '))
b = int(input('podaj liczbe 2: '))

if b<w:
    w,b = b,w
    while w<=b:
        print(w,end=' ')
        w+=1