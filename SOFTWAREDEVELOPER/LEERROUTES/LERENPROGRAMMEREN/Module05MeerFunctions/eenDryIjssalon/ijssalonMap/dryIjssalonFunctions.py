# M05.PA.O2 - Een programma realiseren

# VARIABELEN -------------------------------------------------------------------------------------------------------------

NEE = ['nee', 'n', 'Nee']
JA = ['ja', 'j', 'Ja']
MAXBOLLETJES = 9 # constanten
BOLLETJESBAKJE = {4, 5, 6, 7, 8}  
BOLLETJESBEIDE = {1, 2, 3}        


HOORNTJE = ['hoorntje', 'Hoorntje', 'h']
BAKJE = ['bakje', 'Bakje', 'b']


# FUNCTIONS -------------------------------------------------------------------------------------------------------------

def hoeveelBolletjes(MAXBOLLETJES): #constanten hoeven niet mee geven te worden
    functionAantalBolletjes = True
    while functionAantalBolletjes:

        aantalBolletjesInput = input("Hoeveel bolletjes zou u graag willen? ")

        # checken voor nummer:
        if not aantalBolletjesInput.isdigit():
            print("Dat ken ik niet.")
            continue
        
        #toevoegen voor return:
        aantalBolletjes = int(aantalBolletjesInput)

        # checken voor het juiste aantal:
        if aantalBolletjes >= MAXBOLLETJES:
            print("Zulke grote porties verkopen wij niet.")
 
        else:
            functionAantalBolletjes = False  

    return aantalBolletjes  

# aantalBolletjes = hoeveelBolletjes(MAXBOLLETJES, BOLLETJESBAKJE, BOLLETJESBEIDE, aantalBolletjes)
# print(aantalBolletjes)

def hoorntjeOfBakje(aantalBolletjes):

        # 4 of meer bolletjes
    if aantalBolletjes in BOLLETJESBAKJE and aantalBolletjes not in BOLLETJESBEIDE:
            keuzeHoorntjeBakje = 'bakje'
            print(f"U heeft {aantalBolletjes} bolletjes dus u krijgt een {keuzeHoorntjeBakje}. ")
            # kiezenHoorntjeBakje = False
    else:
        kiezenHoorntjeBakje = True
        while kiezenHoorntjeBakje:
            # 1 t/m 3 bolletjes
                keuzeHoorntjeBakje = str(input("Wilt u een hoorntje of een bakje? "))

                # keuze hoorntje bakje
                if keuzeHoorntjeBakje in HOORNTJE or keuzeHoorntjeBakje in BAKJE:
                    print(f"Oke, u krijgt {aantalBolletjes} bolletjes in een {keuzeHoorntjeBakje}. ")
                    kiezenHoorntjeBakje = False
                else:
                    print("Dat ken ik niet.")
    return keuzeHoorntjeBakje


# keuzeHoorntjeBakje = hoorntjeOfBakje(aantalBolletjes, keuzeHoorntjeBakje)
# print(keuzeHoorntjeBakje)

def meerBestellen(JA, NEE):
    kiezenMeerBestellen = True
    while kiezenMeerBestellen:

        # keuze meer bestellen
        meerBestellenInput = str(input("Wilt u nog meer bestellen? "))
        if meerBestellenInput in JA:
            kiezenMeerBestellen = False
        elif meerBestellenInput in NEE: 
            print("Bedankt en nog een fijne dag verder!")
            kiezenMeerBestellen = False
            return False  #stop programma

        else:
            print("Dat ken ik niet.")
            kiezenMeerBestellen = True
    return True  #continue programma

