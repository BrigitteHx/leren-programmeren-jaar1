# fruitmandopdracht08.py

from fruitmand import fruitmand

totaal_gewicht = 0

watermeloen = {                                                  # watermeloen maken
    "name" : "watermeloen",
    "weight" : 150,
    "color" : "green",
    "round" : True}

fruitmand.append(watermeloen)                                    # watermeloen toevoegen

for i in range(len(fruitmand)):                                  # range voor gehele lijst ( ook watermeloen )
  totaal_gewicht = totaal_gewicht + fruitmand[i]["weight"]       # gewicht + gewicht + gewicht.. enzovoort 
print(f"{totaal_gewicht} gram")                                  # totaal gewicht printen 