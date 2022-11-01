#M04.D01.O5 - Boodschappenlijstje

vraag = str(input("Wilt u iets aan uw boodschappenlijst toevoegen? "))
if vraag == "ja":
    itemslijst = input("Typ wat u toe wilt voegen hier in, vergeet niet om spaties toe te voegen: ")
    boodschappenlijst = itemslijst.split(" ")
    print("\n")
    print("Uw boodschappen lijst: ")
    print("\n")
    for naamitem in boodschappenlijst:
        print(naamitem)
    print("\n")
    print("Nog een fijne dag verder!")
else: 
    print("Oke, fijne dag verder. ")

# eerste poging, niet uitgekomen: 

# lijst = [] 

# while True: 


        # boodschappen = item.split(" ")
        # lijst.append(item)
    #     # boodschappen = item.split("\n")
    # elif vraag == "nee":
    #     # for boodschap in :
    #     print("Uw boodschappen lijst:")
    #     print(lijst)
    #     break 