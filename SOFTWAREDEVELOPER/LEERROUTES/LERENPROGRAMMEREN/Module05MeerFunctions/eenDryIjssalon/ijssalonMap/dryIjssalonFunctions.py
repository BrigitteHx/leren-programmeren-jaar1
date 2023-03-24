# M05.PA.O2 - Een programma realiseren

# VARIABELEN -------------------------------------------------------------------------------------------------------------

MAXBOLLETJES = 9

# FUNCTIONS -------------------------------------------------------------------------------------------------------------

def hoeveelBolletjes():
    while True:
        aantalBolletjesInput = input("Hoeveel bolletjes zou u graag willen? ")
        if not aantalBolletjesInput.isdigit():
            print("Dat ken ik niet.")
        else:
            aantalBolletjes = int(aantalBolletjesInput)
            if aantalBolletjes >= MAXBOLLETJES:
                print("Zulke grote porties verkopen wij niet.")
            else:
                return aantalBolletjes               

def hoorntjeOfBakje(aantalBolletjes):
    if aantalBolletjes > 4:
        keuzeHoorntjeBakje = 'bakje'
        print(f"U heeft {aantalBolletjes} bolletjes dus u krijgt een {keuzeHoorntjeBakje}. ")
    else:
        while True:
            keuzeHoorntjeBakje = input("Wilt u een hoorntje of een bakje? ")
            if keuzeHoorntjeBakje.lower() in ("hoorntje", "bakje"):
                print(f"Oke, u krijgt {aantalBolletjes} bolletjes in een {keuzeHoorntjeBakje}. ")
                return keuzeHoorntjeBakje
            else:
                print("Dat ken ik niet.")

def meerBestellen():
    while True:
        meerBestellenInput = input("Wilt u nog meer bestellen? ")
        if meerBestellenInput.lower() == "ja":
            return True
        elif meerBestellenInput.lower() == "nee":
            print("Bedankt en nog een fijne dag verder!")
            return False
        else:
            print("Dat ken ik niet.")

def functionBonnetje(hoorntjes, bakjes, aantalBolletjes):
    totalH = hoorntjes * 1.25
    totalBa = bakjes * 0.75
    totalBo = aantalBolletjes * 1.10
    totaalAlles = totalH + totalBa + totalBo
    print("----------[Papi Gelato]----------\n")
    print(f"Hoorntjes:  {hoorntjes} voor {round(totalH, 2)}")
    print(f"Bakjes:     {bakjes} voor {round(totalBa, 2)}")
    print(f"Bolletjes:  {aantalBolletjes} voor {round(totalBo, 2)}\n")
    print("--------------------------- +")
    print(f"Totaal:      {round(totaalAlles, 2)}")

def main():
    doorloopSalon = True
    totaalAantalBolletjes = 0
    totaalHoorntjes = 0
    totaalBakjes = 0

    while doorloopSalon:
        aantalBolletjes = hoeveelBolletjes()
        keuzeHoorntjeBakje = hoorntjeOfBakje(aantalBolletjes)
        totaalAantalBolletjes += aantalBolletjes

        if keuzeHoorntjeBakje == "hoorntje":
            totaalHoorntjes += 1
        else:
            totaalBakjes += 1

        if not meerBestellen():
            doorloopSalon = False

    functionBonnetje(totaalHoorntjes, totaalBakjes, totaalAantalBolletjes)

