# challange smartphone

naamiphone = input("Wat is de naam van uw iPhone? " )
prijsiphone = int(input("Hoe duur is uw iPhone? "))

naamsamsung = input("Wat is de naam van uw Samsung? " )
prijssamsung = int(input("Hoe duur is uw Samsung? ")) 

verschil = prijsiphone - prijssamsung

if prijsiphone > prijssamsung and verschil <= 50 : 
    print((f"De {naamiphone} is het duurts, de telefoon kost: {prijsiphone} Euro "))
    print(f"De {naamsamsung} is het goedkoopst, de telefoon kost: {prijssamsung} Euro ")
    print(f"Het advies is dus de {naamiphone} te kopen. ")
elif prijsiphone == prijssamsung :
    print(f"De smartphones zijn even duur: {prijsiphone} Euro ")
    print("Ons advies is om de iPhone te kopen, deze is kwalitatief beter. ")
elif prijsiphone and prijssamsung > 900 :
    print(f"De door u gekozen smartphones: {naamiphone} en {naamsamsung} zijn beide boven 900 euro.")
    print("Het advies is dus geen telefoon te kopen, ze zijn te duur.")
else :
    print(f"De {naamiphone} is het duurts, de telefoon kost: {prijsiphone} Euro ")
    print(f"De {naamsamsung} is het goedkoopst, de telefoon kost: {prijssamsung} Euro ")
    print(f"Het advies is dus de {naamsamsung} te kopen, deze is {verschil} Euro goedkoper. ")


   # laatste uitbreiding nog toevoegen 