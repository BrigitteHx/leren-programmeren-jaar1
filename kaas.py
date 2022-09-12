# kaas

while True :
    vraag1 = input("Is de kaas geel?")
    if vraag1 in ["Yes", "No"] : 
        break

if vraag1 == "Yes" :
    vraag2 = input("Zitten er gaten in?")

if vraag2 == "No" : 
    vraag3 = input("Is de kaas hard als steen?")
elif vraag2 == "Yes" : 
    vraag4 = input("Is de kaas belagelijk duur?")

if vraag3 == "Yes" : 
    print("Parmigiano")
elif vraag3 == "No" :
    print("Goudse Kaas")

if vraag4 == "Yes" : 
    print("Emmenthaler")
elif vraag4 == "No" : 
    print("Leerdammer")




