# 5
deszcz = input("Pada deszcz? (Tak/Nie) :")
deszcz = str(deszcz)

autobus = input("Jest autobus? (Tak/Nie) :")
autobus = str(autobus)

if deszcz.strip().lower() == 'tak':
    deszcz = True
else:
    deszcz = False

if autobus.strip().lower() == 'tak':
    autobus = True
else:
    autobus = False

if deszcz and autobus:
    print("Weź parasol")
    print("Dostaniesz się na uczelni")
elif deszcz and not autobus:
    print("Nie dostaniesz się na uczelnię")
elif not deszcz and autobus:
    print("Dostaniesz się na uczelnie")
    print("Miłego dnia i pięknej pogody")
else:
    print("Coś jest nie tak!!!")
