from ast import If
from random import randint

a = randint(0,100)
b = randint(0,100)

print(a,b)

if a < b and a < 50:
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")

elif a < 30 or b < 30:
    print("Eine der beiden kleiner als 30")

elif a < 50 and b != 50:
    print("Erste Zahl klein, zweite kein 50iger")