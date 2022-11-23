#Proef A - Lootjes verdeler

print("Welkom tot de loostjes verdeler.")

namenlijst = []
aantalnamen = 0
nameninvoer = 0

while nameninvoer == 0:
    keuzetoevoegen = input("Wilt U een nieuwe unieke naam toevoegen? ").lower()
    if keuzetoevoegen == "ja":
        nameninvoer =+ 1

if nameninvoer == 1:
    naaminput = input("Welke naam wilt u toevoegen? ")
    namenlijst.append(naaminput)
    aantalnamen =+ 1
    nameninvoer = 0

