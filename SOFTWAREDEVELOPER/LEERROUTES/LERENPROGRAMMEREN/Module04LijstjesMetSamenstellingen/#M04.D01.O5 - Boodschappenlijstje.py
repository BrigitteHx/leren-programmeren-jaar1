#M04.D01.O5 - Boodschappenlijstje


# -----------------------------------------------------------------------------------

# vraag = str(input("Wilt u iets aan uw boodschappenlijst toevoegen? "))
# if vraag == "ja":
#     itemslijst = input("Typ wat u toe wilt voegen hier in, vergeet niet om spaties toe te voegen: ")
#     boodschappenlijst = itemslijst.split(" ")
#     print("\n")
#     print("Uw boodschappen lijst: ")
#     print("\n")
#     for naamitem in boodschappenlijst:
#         print(naamitem)
#     print("\n")
#     print("Nog een fijne dag verder!")
# else: 
#     print("Oke, fijne dag verder. ")

# ----------------------------------------------------------------------------------- 

lijst = [] 
amount = 1

while True: 

 vraag = str(input("Wilt u iets aan uw boodschappenlijst toevoegen? "))
 vraag.lower()
 if vraag == "ja": 
    item = input("Wat wilt u toe voegen aan uw boodschappenlijst? ")
    if item == item:
        amount =+ 1
    lijst.append(item)
 elif vraag == "nee":
    print("Uw boodschappen lijst:")
    for x in lijst: 
        print(amount, x)
    break   
