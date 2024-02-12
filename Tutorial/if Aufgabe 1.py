from ast import If
from random import randint

a = randint(0,100)

print(a)

if a < 10:
    print("Mini")
elif a >=20 and a <=50:
    print("Med")
else:
    print("Large")