# fruitmandopdracht09.py

from fruitmand import fruitmand

for i in range(len(fruitmand)):
    if fruitmand[i]['name'] == 'druif':
        fruitmand.pop(i)
        break

kleuren = []

for fruit in fruitmand:
    if (fruit['color']) not in kleuren:
        kleuren.append(fruit['color'])
print(kleuren)  