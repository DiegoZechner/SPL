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

    Userinput = input("Wählen Sie ihre Aktion aus: ")
    print("-------------------------")

    if Userinput == "1":
        print("Geben Sie das gewollte Geld ein")
        Ebetrag = int(input("Gewünschter Betrag: "))
        Kontostand += Ebetrag
        print("Sie haben", Ebetrag, "€ Eingezahlt.")
        print("Ihr Kontostand beträgt:",Kontostand)
        print("-------------------------")

    if Userinput == "2":
        print("Wie viel möchten Sie abheben?")
        Abetrag = int(input("Gewünschter Betrag: "))
        Kontostand -= Abetrag
        print("Sie haben", Abetrag, "€ Eingezahlt.")
        print("Ihr Kontostand beträgt:",Kontostand)
        print("-------------------------")

    if Userinput == "3":
        print("Ihr Kontostand beträgt:",Kontostand)
        print("-------------------------")

    if Userinput == "4":
        print("Entnehmen Sie ihre.")
        break