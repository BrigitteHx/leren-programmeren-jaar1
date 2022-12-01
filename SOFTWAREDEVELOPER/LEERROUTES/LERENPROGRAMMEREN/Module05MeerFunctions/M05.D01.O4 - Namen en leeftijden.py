# M05.D01.O4 - Namen en leeftijden



    # name = input('Enter your name and press ENTER')
    # age = input('Enter your birth_year and press ENTER')
    
    # name.append(name_list)
    # age_list=age.split()
    
    # print(f'{name_list} is {age_list}jaar oud')
    # finalname = name[1][0]
    # finalage = age[1][0]

    # print(name)
    # print(surname)
    # print(age)

namen_lijst , leeftijd_lijst = [], []

lijst_started = ""
while lijst_started == "":
    lijst_started = input("Wilt U de lijst maken? ").lower()

def namen_leeftijden_lijst():
    if lijst_started == "ja":
        naam = input("Voer een naam in en enter. ")
        leeftijd = input("Voer de bijbehorende leeftijd in en klik enter. ")
        
        leeftijd_lijst.append(leeftijd)
        namen_lijst.append(naam)
        lijst_started = ""
    else: 
        for tel, el in enumerate(namen_lijst):
            print(el, "is", leeftijd_lijst[tel], "jaar oud.")


            
            # print(f"{tel} is {namen_lijst} jaar oud.")
            # namen_lijst.pop[0]
            # leeftijd_lijst.pop[0]

#  for tel, el in enumerate(lijst):
#     print(el, lijst2[tel])

namen_leeftijden_lijst()


# if lijststarted == "ja":
#     namen_leeftijden_lijst()

# else: 

