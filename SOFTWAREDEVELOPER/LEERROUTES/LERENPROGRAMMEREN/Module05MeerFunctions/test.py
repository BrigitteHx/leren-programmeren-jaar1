# # for = element bijhouden/ uit verzamling halen, variabele houd bij, enumerta zowel element als posititie 
# # lijst = ["1","2","3","aap","noot","mies"]
# # lijst2 = [12, 13, 14, 15, 16, 17]

# for tel, el in enumerate(range(5)):
#     print(el, tel)


# # for tel, el in enumerate(lijst):
# #     print(el, lijst2[tel])

# mijn_tuple = (1, 5, 7, 9)
# # for x in (1, 5, 7, 9):
# #    pass
# #
# for x in mijn_tuple:
#      print(x)

# # for x in range(215, 250, 2):
# #     print(x)

# # for x in (215, 217):
# #     pass

# mijn_lijst = list(range(5))
# print(mijn_lijst)

#------------------------------------------------------------------------------------------------
landen_verdelen = True 

while landen_verdelen:
    landen_door_elkaar = random.sample(groep_a, len(groep_a))
    landen_verdelen = False
    for i in range(len(groep_a)):
        if landen_door_elkaar[i] == groep_a[i]:   
            landen_verdelen = True                  

for land in range(len(groep_a)):                 
    wedstrijd_verdeling.update({groep_a[land] : landen_door_elkaar[land]}) 

print(f"De landen die tegen elkaar moeten spelen: {wedstrijd_verdeling}")
