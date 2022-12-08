#wk_challenge.py 
# import random

wedstrijd_gewonnen = 3
wedstrijd_verloren = 0
groep_a = []
wedstrijd_verdeling = {}
landen_invoeren = True

while landen_invoeren:
    keuze_invoeren = input("Wilt u een voetbal land toevoegen? ").lower()
    if keuze_invoeren == "ja":
        land_invoer = input("Voer een land in: ")
        if land_invoer not in groep_a:
            groep_a.append(land_invoer)
    elif keuze_invoeren == "nee" and len(groep_a) < 3:
        print("Niet genoeg landen, u moet 3 of meer deelnemers hebben. ")
    else:
        landen_invoeren = False

print(f"Dit is groep A {groep_a}")

# landen_verdelen = True 

# while landen_verdelen:
#     landen_door_elkaar = random.sample(groep_a, len(groep_a))
#     landen_verdelen = False
#     for i in range(len(groep_a)):
#         if landen_door_elkaar[i] == groep_a[i]:   
#             landen_verdelen = True                  

# for land in range(len(groep_a)):                 
#     wedstrijd_verdeling.update({groep_a[land] : landen_door_elkaar[land]}) 

# print(f"De landen die tegen elkaar moeten spelen: {wedstrijd_verdeling}")