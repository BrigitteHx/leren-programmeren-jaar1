# challange smartphone

naamsmartphone1 = input("Wat is de naam van uw iPhone? " )
smarthphone1 = int(input("Hoe duur is uw iPhone? "))

naamsmsartphone2 = input("Wat is de naam van uw Samsung? " )
smartphone2 = int(input("Hoe duur is uw Samsung? ")) 

if smarthphone1 > smartphone2 : 
    print( print(f"De {naamsmartphone1} is het duurts, de telefoon kost: {smarthphone1} Euro "))
    print(f"De {naamsmsartphone2} is het goedkoopst, de telefoon kost: {smartphone2} Euro ")
    print(f"Het advies is dus de {naamsmsartphone2} te kopen, deze is {smarthphone1 - smartphone2} Euro goedkoper. ")
elif smarthphone1 < smartphone2 :
    print(f"De {naamsmsartphone2} is het duurts, de telefoon kost: {smartphone2} Euro ")
    print(f"De {naamsmartphone1} is het goedkoopst, de telefoon kost: {smarthphone1} Euro ")
    print(f"Het advies is dus de {naamsmartphone1} te kopen, deze is {smartphone2 - smarthphone1} Euro goedkoper. ")
elif smarthphone1 == smartphone2 :
    print(f"De smartphones zijn even duur: {smarthphone1} Euro ")
    print("Ons advies is om de iPhone te kopen, deze is kwalitatief beter. ")


if smarthphone1 and smartphone2 > 900 :
   print(f"De door u gekozen smartphones: {naamsmartphone1} en {naamsmsartphone2} zijn beide boven 900 euro.")
   print("Het advies is dus geen telefoon te kopen, ze zijn te duur.")

   # laatste uitbreiding nog toevoegen 