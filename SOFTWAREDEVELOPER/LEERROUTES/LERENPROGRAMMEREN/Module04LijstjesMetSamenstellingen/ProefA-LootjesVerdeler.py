#Proef A - Lootjes verdeler

import random

namen_lijst = []
lootjes_eind = {}
aantal_namen = 0
programma = True

print("Welkom tot de loostjes verdeler.")

while programma:
    keuze_naam = input("Wilt u een naam toevoegen?").lower()
    if keuze_naam == "ja":
        naam_invoer = input("Voer een unieke naam in: ")
        if naam_invoer in namen_lijst:
            programma = True
        else: 
            namen_lijst.append(naam_invoer)
            aantal_namen += 1 
            programma = True
    elif keuze_naam == "nee" and aantal_namen < 3:
        print("Niet genoeg namen, u moet 3 of meer deelnemers hebben. ")
        programma = True
    elif keuze_naam == "nee" and aantal_namen >= 3:
        programma = False
        
lootjes_verdelen = True 

while lootjes_verdelen:
    namen_door_elkaar = random.sample(namen_lijst, len(namen_lijst))
    lootjes_verdelen = False
    for i in range(len(namen_lijst)):
        if namen_door_elkaar[i] == namen_lijst[i]:   # vragen index ivm andere naam geeft erorr
            namen_door_elkaar = True                 # checken of namen niet hetzelfde zijn en andersop nieuw

for naam in range(len(namen_lijst)):                 # hier werkt "naam" ipv index wel
    lootjes_eind.update({namen_lijst[naam] : namen_door_elkaar[naam]}) # lijst aan nieuwe directory om te printen

print(lootjes_eind)

# sample() is an inbuilt function of random module in Python that returns a particular length list of items chosen from the sequence i.e. list, tuple, string or set. Used for random sampling without replacement.