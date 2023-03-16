#  Een Dry Ijssalon, M05.PA.O2 - Een programma realiseren

from dryIjssalonFunctions import *

print("Welkom bijPapi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.\n")
doorloopSalon = True
while doorloopSalon:
       
    aantalBolletjes = 0
    keuzeHoorntjeBakje = ""

    aantalBolletjes = hoeveelBolletjes(MAXBOLLETJES, BOLLETJESBAKJE, BOLLETJESBEIDE, aantalBolletjes)
    keuzeHoorntjeBakje = hoorntjeOfBakje(aantalBolletjes, keuzeHoorntjeBakje)
    functionAantalBolletjes = meerBestellen(JA, NEE)
    if functionAantalBolletjes == True:
        doorloopSalon = True
    if functionAantalBolletjes != True:
        doorloopSalon = False


