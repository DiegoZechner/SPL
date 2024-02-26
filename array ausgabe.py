from ast import If
from random import randint

mylist = ["hans", "peter", "susi"]

a = randint(1, 3)

print(a)

if a == 1:
    print(mylist[0])

elif a == 2:
    print(mylist[1])

elif a == 3:
    print(mylist[2])