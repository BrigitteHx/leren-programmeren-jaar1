# opgave 13 

from data import *
from functions import *


def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold ,getInterestingInvestors(investors))
    goldCut = round(getAdventurerCut(profitGold,investorsCuts,len([mainCharacter]+adventuringFriends+getAdventuringInvestors(investors))),2)

    donateGold = 10

    # verdeel de uitkomsten
    for person in people:
        #code aanvullen
        startAdventure = getPersonCashInGold(person["cash"])
        endAdventure =+ startAdventure
        if person == mainCharacter:
            endAdventure =+ round((startAdventure+goldCut) + (donateGold*len(adventuringFriends)),2)
            # eindbedrag = start bedrag + jou deel + donation (x het aantal vriended)
        if person in adventuringFriends:
            endAdventure =+ round((startAdventure+goldCut)-donateGold,2)
            # eindbedrag = startbedrag + jou deel - 1x donation (want niet hoofd persoon), vrienden dus geen inversteer deel terug
        if "profitReturn" in person:
            if person in getInterestingInvestors(investors):
                # investors die mee gaan:
                if person in getAdventuringPeople(investors):
                    endAdventure =+ round((profitGold/100)*person["profitReturn"]+startAdventure+goldCut,2)
                    # eindbedrag = profit / 100 (want%) x investors profitreturn + start + goldcut 
                else:
                    endAdventure =+ round((profitGold/100)*person["profitReturn"]+startAdventure,2)
                    # eindbedrag = profit / 100 (want%) x investors profitreturn + start (geen goldcut want ging niet mee)
        earnings.append({
            'name'   : person["name"],
            'start'  : startAdventure,
            'end'    : endAdventure
        })