# 6
arg1 = input("Podaj arg1: ")
arg1 = float(arg1)

oper = input("Podaj operacja (+,-,*,/,%) : ")
oper = str(oper).strip()

arg2 = input("Podaj arg2: ")
arg2 = float(arg2)

if oper == "+":
    rezult = arg1 + arg2
elif oper == "-":
    rezult = arg1 - arg2
elif oper == "*":
    rezult = arg1 * arg2
elif oper == "/":
    rezult = arg1 / arg2
elif oper == "%":
    rezult = arg1 % arg2
else:
    rezult = "Coś jest nie tak!"

if rezult == "Coś jest nie tak!":
    print(arg1, oper, arg2, ' - ', rezult)
else:
    print(arg1, oper, arg2, ' = ', rezult)
