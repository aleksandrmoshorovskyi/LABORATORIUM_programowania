w = int(input('podaj liczbe 1: '))
b = int(input('podaj liczbe 2: '))

if b<w:
    w,b = b,w
    while w<=b:
        w += 1
        if w%2 == 0: continue
        print(w,end=' ')
#       w += 1
