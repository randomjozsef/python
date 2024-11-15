kezd = 1
veg = 100
ismet = True
tipp = int((veg - kezd) / 2) + kezd

def talalt():
    print("Nagyon örülök!")
    global ismet
    ismet = False

def sok():
    global tipp
    global veg
    global kezd
   
    v = tipp
    tipp = int((veg - tipp) / 2) + kezd
    veg = v
    if v == tipp:
        print("Csaltál a válaszokban!")

def keves():
    global tipp
    global veg
    global kezd

    kezd = tipp
    tipp = int((veg - tipp) / 2) + kezd
    if kezd == tipp:
        print("Csaltál a válaszokban!")

while ismet:
    #tipp = int(veg / 2)
    #print("A tippem: " + str(tipp))
    print(f"A tippem: {tipp}")
    print("Kérem a válaszod!\n1. sok\n2. kevés\3 ")
    valasz = input("1 vagy 2 vagy 3 vagy : ")

    elif valasz == "1":
        sok()
    elif valasz == "2":
        keves()
    elif valasz == "3":
        talalt()
    
    else:
        print("\n\nHibás válasz!\n\n")