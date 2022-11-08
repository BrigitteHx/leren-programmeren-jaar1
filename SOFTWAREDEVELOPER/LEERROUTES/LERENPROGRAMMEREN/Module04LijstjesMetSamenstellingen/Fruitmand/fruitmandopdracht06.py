# fruitmandopdracht06.py

from fruitmand import fruitmand


fruit = fruitmand[1]['weight']
# appel = 0

for fruit in fruitmand:
    if fruit['name'] == "appel":
        print(fruit['weight'])