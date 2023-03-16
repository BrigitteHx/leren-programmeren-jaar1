# M05.PA.O2 - Een programma realiseren

# VARIABELEN -------------------------------------------------------------------------------------------------------------

NEE = ['nee', 'n', 'Nee']
JA = ['ja', 'j', 'Ja']
MAXBOLLETJES = 9 
BOLLETJESBAKJE = {4, 5, 6, 7, 8}  
BOLLETJESBEIDE = {1, 2, 3}        
aantalBolletjes = 0

HOORNTJE = ['hoorntje', 'Hoorntje', 'h']
BAKJE = ['bakje', 'Bakje', 'b']
keuzeHoorntjeBakje = ""

# FUNCTIONS -------------------------------------------------------------------------------------------------------------

def hoeveelBolletjes(MAXBOLLETJES, BOLLETJESBAKJE, BOLLETJESBEIDE, aantalBolletjes):
    functionAantalBolletjes = True
    while functionAantalBolletjes:

        aantalBolletjesInput = input("Hoeveel bolletjes zou u graag willen? ")

        # checken voor nummer:
        if not aantalBolletjesInput.isdigit():
            print("Dat ken ik niet.")
            continue
        
        #toevoegen voor return:
        aantalBolletjesInput = int(aantalBolletjesInput)
        aantalBolletjes += aantalBolletjesInput

        # checken voor het juiste aantal:
        if aantalBolletjesInput >= MAXBOLLETJES:
            print("Zulke grote porties verkopen wij niet.")
            functionAantalBolletjes = False  
        elif aantalBolletjesInput in BOLLETJESBAKJE or aantalBolletjesInput in BOLLETJESBEIDE:
            # print("goed!")
            functionAantalBolletjes = False  

    return aantalBolletjes

# aantalBolletjes = hoeveelBolletjes(MAXBOLLETJES, BOLLETJESBAKJE, BOLLETJESBEIDE, aantalBolletjes)
# print(aantalBolletjes)

def hoorntjeOfBakje(aantalBolletjes, keuzeHoorntjeBakje):
    kiezenHoorntjeBakje = True
    while kiezenHoorntjeBakje:
        if aantalBolletjes in BOLLETJESBAKJE and aantalBolletjes not in BOLLETJESBEIDE:
            print(f"U heeft {aantalBolletjes} bolletjes dus u krijgt een bakje. ")
            kiezenHoorntjeBakje = False
    
        if aantalBolletjes in BOLLETJESBEIDE and aantalBolletjes not in BOLLETJESBAKJE:
            keuzeHoorntjeBakjeInput = str(input("Wilt u een hoorntje of een bakje? "))
            keuzeHoorntjeBakje += keuzeHoorntjeBakjeInput
            if keuzeHoorntjeBakje in HOORNTJE or keuzeHoorntjeBakje in BAKJE:
                print(f"Oke, u krijgt {aantalBolletjes} bolletjes in een {keuzeHoorntjeBakje}. ")
                kiezenHoorntjeBakje = False
            elif keuzeHoorntjeBakje not in HOORNTJE and keuzeHoorntjeBakje not in BAKJE:
                print("Dat ken ik niet.")
                keuzeHoorntjeBakje = ""
                kiezenHoorntjeBakje = True
    return keuzeHoorntjeBakje

# keuzeHoorntjeBakje = hoorntjeOfBakje(aantalBolletjes, keuzeHoorntjeBakje)
# print(keuzeHoorntjeBakje)

def meerBestellen(JA, NEE):
    functionAantalBolletjes = True
    kiezenMeerBestellen = True
    while kiezenMeerBestellen:
        meerBestellenInput = str(input("Wilt u nog meer bestellen? "))
        if meerBestellenInput in JA:
            kiezenMeerBestellen = False
        elif meerBestellenInput in NEE: 
            print("Bedankt en nog een fijne dag verder!")
            kiezenMeerBestellen = False

        else:
            print("Dat ken ik niet.")
            kiezenMeerBestellen = True
    return functionAantalBolletjes

# functionAantalBolletjes = meerBestellen(JA, NEE)

# if functionAantalBolletjes == True:
#     hoeveelBolletjes(MAXBOLLETJES, BOLLETJESBAKJE, BOLLETJESBEIDE, aantalBolletjes)

doorloopSalon = True
while doorloopSalon:
       
    aantalBolletjes = 0
    keuzeHoorntjeBakje = ""

    aantalBolletjes = hoeveelBolletjes(MAXBOLLETJES, BOLLETJESBAKJE, BOLLETJESBEIDE, aantalBolletjes)
    keuzeHoorntjeBakje = hoorntjeOfBakje(aantalBolletjes, keuzeHoorntjeBakje)
    functionAantalBolletjes = meerBestellen(JA, NEE)
    if functionAantalBolletjes == True:
        doorloopSalon = True
    else:
        doorloopSalon = False

