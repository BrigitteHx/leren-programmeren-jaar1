# M05.D01.O4 - Namen en leeftijden V2

namen_lijst, leeftijd_lijst = [], []

def namen_leeftijden_lijst():
    start = True
    while start:
        start = input("Wilt U de lijst maken? ").lower()
        
        if start == "ja":
            naam = input("Voer een naam in en enter. ")
            leeftijd = input("Voer de bijbehorende leeftijd in en klik enter. ")
        
            leeftijd_lijst.append(leeftijd)
            namen_lijst.append(naam)
            start = True
        else: 
            for tel, el in enumerate(namen_lijst):
                print(el, "is", leeftijd_lijst[tel], "jaar oud.")
    
namen_leeftijden_lijst()