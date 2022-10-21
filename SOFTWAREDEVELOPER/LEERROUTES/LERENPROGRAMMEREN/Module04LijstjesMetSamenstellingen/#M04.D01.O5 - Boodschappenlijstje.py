#M04.D01.O5 - Boodschappenlijstje

lijst = []

while True:
    vraag = str(input("Wilt u iets aan uw boodschappenlijst toevoegen? "))
    if vraag == "ja":
        item = input("Wat wilt u aan uw boodschappenlijstje toevoegen? ")
        # boodschappen = item.split(" ")
        lijst.append(item)
        boodschappen = item.split(" ")
    elif vraag == "nee":
        # for boodschap in :
        print("Uw boodschappen lijst:")
        print(lijst)
        break 


input_string = #input("Enter all family members name separated by space  ")
# # Split string into words
# family_list = input_string.split(" ")

# print("\n")
# # Iterate a list
# print("Printing all family member names")
# for name in family_list:
#     print(name)