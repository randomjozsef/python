import random


def beker():
    ismeteld = True
    while ismeteld:
        be = input("Kérek egy egész számot 1 és 100 között : ")
        if (be.isnumeric()) :
            szam =  int(be)
            ismeteld = False
        else:
            print("Nem jó formátum")
    return szam


def jatek():
    ismetles = True
    lepesek = 0
    gondolt = random.randint(1,100)
    while ismetles:
        tipp = beker()
        lepesek += 1
        if (tipp == gondolt):
            print("Talált!" + str(lepesek) + " Próbálkozásod volt")
            ismetles = False           
        elif (tipp < gondolt):
            print("A szám kicsi!")
        else :
            print("A szám nagy!")



valasz = input("Akarsz velem játszani? (I/N): ").lower()
while valasz == "I" or valasz == "igen":
    jatek()
    valasz = input("Akarsz velem még játszani? (I/N): ").lower()