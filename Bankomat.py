from ast import If
from random import randint


Kontostand = 0

while True:
    print("Willkommen zur Volksbank")
    print("1.Einzahlen")
    print("2.Abheben")
    print("3.Kontostand")
    print("4.Beenden")
    print(" ")

    Userinput = input("Wählen Sie ihre Aktion aus")
    print("-------------------------")

    if Userinput == "1":
        print("Geben Sie das gewollte Geld ein")
        betrag = int(input("Geldmenge"))
        Kontostand += betrag
        print("Sie haben x € eingezahlt.")
    

   