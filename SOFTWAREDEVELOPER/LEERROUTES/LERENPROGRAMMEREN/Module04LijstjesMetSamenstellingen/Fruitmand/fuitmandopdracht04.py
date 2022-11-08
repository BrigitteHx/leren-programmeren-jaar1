# fruitmandopdracht04.py

from fruitmand import fruitmand
import random 

hoeveelheid = int(input("Voer hier een aantal in: "))
random_fruit = random.randint(0,7)

for i in range (0,hoeveelheid):
    print(fruitmand[random_fruit]['name'])

# --------------------------------------------------------          oude code

# fruit = fruitmand[0]['name']

# for fruit in fruitmand:
#     print(fruit['name'])
