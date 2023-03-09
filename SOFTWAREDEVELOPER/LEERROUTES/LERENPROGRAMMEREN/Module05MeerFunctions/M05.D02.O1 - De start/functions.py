import time
from termcolor import colored
from data import *
##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount / 10      # want 10 koper / 10 = 1 zilver

def silver2gold(amount:int) -> float:
    return amount / 5       # want 5 zilver / 5 = 1 goud

def copper2gold(amount:int) -> float:
    silver = copper2silver(amount)
    return silver2gold(silver)      # want eerst van koper -> silver en dan van silver -> gold (volgens schema opdracht)

def platinum2gold(amount:int) -> float:
    return amount * 25      # want 1 platinum * 25 = 25 goud 

def getPersonCashInGold(personCash:dict) -> float:
    gold = personCash['gold']
    # gold += copper2silver(personCash['']) -> niet goud dus niet nodig 
    gold += silver2gold(personCash['silver'])
    gold += copper2gold(personCash['copper'])
    gold += platinum2gold(personCash['platinum'])
    return gold 

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    TotalCopper = JOURNEY_IN_DAYS * (people * COST_FOOD_HUMAN_COPPER_PER_DAY)
    gold = copper2gold(TotalCopper)
    TotalCopper = JOURNEY_IN_DAYS * (horses * COST_FOOD_HORSE_COPPER_PER_DAY)
    gold += copper2gold(TotalCopper)
    return round(gold, 2)
    
# (JOURNEY_IN_DAYS * (people *COST_FOOD_HUMAN_COPPER_PER_DAY)) + (JOURNEY_IN_DAYS * (horses * COST_FOOD_HORSE_COPPER_PER_DAY)) werkt niet -> vragen

##################### M04.D02.O5 #####################

#     NieuweLijst = []
#     for x in list:
#         if x[key] == value:
#             NieuweLijst.append(x)
#     return NieuweLijst

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    NieuweLijst = []
    for nummer in range(len(list)):
        if list[nummer][key]==value:
            NieuweLijst.append(list[nummer])
    return NieuweLijst

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends:list) -> int:
    return getShareWithFriends(friends, "shareWith", True)

def getAdventuringFriends(friends:list) -> list:
    NieuweLijst = []
    for nummer in range(len(friends)):
        if friends[nummer]["adventuring"] and friends[nummer]["shareWith"]:
            NieuweLijst.append(friends[nummer]["name"])
        # if friends[nummer]["shareWith"]:
        #     NieuweLijst.append(friends[nummer]["name"])
    return NieuweLijst

##################### M04.D02.O6 #####################

import math

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people/2)
# want 2 personen per paard

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people/3)
# want 3 personen per tent

def getTotalRentalCost(horses:int, tents:int) -> float:
    totalTents = math.ceil(JOURNEY_IN_DAYS/7) * (tents * COST_TENT_GOLD_PER_WEEK)
    totalHorses = horses * (JOURNEY_IN_DAYS * COST_HORSE_SILVER_PER_DAY)
    return totalTents + silver2gold(totalHorses)
# The math.ceil() method rounds a number UP to the nearest integer, if necessary, and returns the result.
# dagen : 7 want tent huren for 1 week, aantal tenten * prijs
# paarden * aantal dagen * prijs geeft totaal  

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    ItemsAsText = []
    for item in items:
        ItemsAsText.append(f"{item['amount']}{item['unit']} {item['name']}")
    return ', '.join(ItemsAsText)

# .join functie: Join all items in a tuple into a string, using a hash character as separator

def getItemsValueInGold(items:list) -> float:
    TotalPrice = float()

    for item in items:
        amount = item['amount']
        price = item['price']['amount']

        PriceType = item['price']['type']

        if PriceType == 'copper':
            TotalPrice += amount * copper2gold(price)

        if PriceType == 'silver':
            TotalPrice += amount * silver2gold(price)

        if PriceType == 'platinum':
            TotalPrice += amount * platinum2gold(price)

        else:
            TotalPrice += price
    return TotalPrice

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    TotalGold = 0
    for person in people:
        TotalGold += person['cash']['gold']
        TotalGold += platinum2gold(person['cash']['platinum'])
        TotalGold += silver2gold(person['cash']['silver'])
        TotalGold += copper2gold(person['cash']['copper'])
    return TotalGold
 
    # TotalGold = 0

    # for person in range(len(people)):
    #     TotalGold += platinum2gold(person['cash']['platinum'])
    #     TotalGold += silver2gold(person['cash']['silver'])
    #     TotalGold += copper2gold(person['cash']['copper'])
        
    #     TotalGold += person['cash']['gold']
    # return TotalGold
        
    # PriceType = people[nummer]['cash'] 
    # for nummer in range(len(people)):
    #     if PriceType == 'platinum':
    #         TotalGold += platinum2gold('platinum')

##################### M04.D02.O9 ##################### 

def getInterestingInvestors(investors:list) -> list:
    YesInvestor = []
    for investor in investors:
        if investor['profitReturn'] <= 10:
            YesInvestor.append(investor)
    return YesInvestor

def getAdventuringInvestors(investors: list) -> list:
    investors = getInterestingInvestors(investors)
    AdventuringInvestor = []
    for investor in investors:
        if investor['adventuring']:
            AdventuringInvestor.append(investor)
    return AdventuringInvestor

# niet werkende maar andere optie 
# def getTotalInvestorsCosts(investors:list, gear:list) -> float:
#     rentalCost = getTotalRentalCost(1,1)
#     foodCost = getJourneyFoodCostsInGold(1,1)
#     inverstors= getAdventuringInvestors(investors)
#     totalCosts = (getItemsValueInGold(gear)  + rentalCost + foodCost) * len(investors)
#     return totalCosts

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    totalCosts = 0
    investors = getAdventuringInvestors(investors)
    for investor in investors:
        totalCosts += getItemsValueInGold(gear) # get gear costs for every inverstor
    totalCosts += getTotalRentalCost(len(investors), len(investors)) # get rental costs for every investor
    totalCosts += getJourneyFoodCostsInGold(len(investors), len(investors)) # get total costs for every investor 
    # print(totalCosts)
    return totalCosts
# vragen want test is niet goed maar methode werkt wel 

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    costsHumans = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT*people)
    costsHorses = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT*horses)
    totalCosts = costsHumans + costsHorses
    # totalDays = leftoverGold/totalCosts # goud : totaal = max dagen mogelijk 
    # return totalDays
    try:
        totalNights = leftoverGold // totalCosts
    except: 
        totalNights = 0
    return totalNights

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    costHumans = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)*people 
    costsHorses = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)*horses
    totalCostsPerNight = costsHorses + costHumans
    return round(totalCostsPerNight*nightsInInn,2)

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:

    profitInvestors = []
    adventuringInvestors = getInterestingInvestors(investors)
    for x in range (len(adventuringInvestors)):
        investorsCuts = round(profitGold / 100 * adventuringInvestors[x][ 'profitReturn'],2)
        profitInvestors.append(investorsCuts)
        # profitInvestors.append(round((profitGold/100) * investors[x]["profitReturn"],2)) 
    return profitInvestors

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:

    for gold in range(len(investorsCuts)):
        profitGold = profitGold - investorsCuts[gold]
    # adventuresCut =+ profitGold/fellowship
    # adventuresCut = round(adventuresCut,2)
    adventuresCut = round(profitGold / fellowship ,2)
    # print(adventuresCut)
    return adventuresCut

##################### M04.D02.O13 #####################

# VERSION 1
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
    return earnings

# feedback Israa:
# volgens mij je code is helemaal goed, de enige die misschien fout ging is dat je bij de earnings moet ook mensen die niet mee hebben gedaan in de reis hebben en hun end cash is dus hetzelfd als hun start cash
# dus die zijn investerso die vroegen meer dan 10% of friends die niet sharewith en adventuring op true hebben
# dus bij de earnings moeten alle namen van friends en investors en dus niet allen interesting investors en adventuring friends
# ik weet het niet of mij  uitleg duidelijk was, maar als niet kan ik ook een stukje code laten zien over wat ik bedoel

# ------------------------------------------------------------------------------------------------------------------------------------------------
 
# VERSION 2 (WERKT NIET)

# def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
#     people = [mainCharacter] + friends + investors
#     earnings = []

#     # haal de juiste inhoud op
#     adventuringFriends = getAdventuringFriends(friends)
#     interestingInvestors = getInterestingInvestors(investors)
#     adventuringInvestors = getAdventuringInvestors(investors)
#     # investorsCuts = getInvestorsCuts(profitGold ,getInterestingInvestors(investors))
#     # goldCut = round(getAdventurerCut(profitGold,investorsCuts,len([mainCharacter]+adventuringFriends+getAdventuringInvestors(investors))),2)

#     people = [mainCharacter] + friends + investors 
#     peopleTotal = [mainCharacter] + adventuringFriends + adventuringInvestors
#     # donateGold = 10
#     donateGold = len(adventuringFriends) * 10
#     adventuresCut = (profitGold - sum(getInvestorsCuts(profitGold,investors)) ) / len(peopleTotal)
#     gold = 0

#     # verdeel de uitkomsten
#     for person in range(len(people)):
#         #code aanvullen

#         startAdventure = round(getPersonCashInGold(people[person]['cash']),2)
#         endAdventure = startAdventure

#         # main character
#         if people[person] in [mainCharacter]:
#             endAdventure += donateGold + adventuresCut
#         # investors 
#         elif people[person] in [investors]:
#             # investors die mee gingen
#             if people[person] in interestingInvestors and people[person] in adventuringInvestors:
#                 gold = round(profitGold / 100 * people[person][ 'profitReturn'],2)
#                 endAdventure += gold + adventuresCut
#             # investors die niet mee gingen
#             elif people[person] in interestingInvestors: # deze mist bij andere methode
#                 gold = round(profitGold / 100 * people[person][ 'profitReturn'],2)
#                 endAdventure += gold
#         # friends die meegingen
#         elif people[person] in [friends]:
#             if people[person] in adventuringFriends:
#                 endAdventure += adventuresCut - 10
        
#         earnings.append({
#                 'name'   : people[person]['name'],
#                 'start'  : round(startAdventure),
#                 'end'    : round(endAdventure)
#             })  
#     return earnings

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()