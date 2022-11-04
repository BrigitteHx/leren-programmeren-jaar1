#klassen opdracht

import random

naam = input("wat is je naam? ")
hoeveel_complimenten = int(input("hoeveel complimenten wil je? "))

complimenten = ["je bent mooi", "je bent aardig", "je bent slim", "je bent geweldig", "je bent speciaal"]

complimentencopy = complimenten[:]          # copy
random.shuffle (complimentencopy)           # random keuze shuffelen 
for i in range(hoeveel_complimenten):       
    print(f"{complimentencopy.pop()} {naam}")           # niet dezelde kiezen/ vw van lijst 
    if complimentencopy == []:
        complimentencopy = complimenten     # nieuwe random lijst genereren 