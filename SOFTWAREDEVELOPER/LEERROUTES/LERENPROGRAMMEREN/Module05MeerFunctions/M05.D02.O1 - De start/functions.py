import time
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY

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
        if friends[nummer]["adventuring"]:
            NieuweLijst.append(friends[nummer]["name"])
        if friends[nummer]["shareWith"]:
            NieuweLijst.append(friends[nummer]["name"])
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

        elif PriceType == 'silver':
            TotalPrice += amount * silver2gold(price)

        elif PriceType == 'platinum':
            TotalPrice += amount * platinum2gold(price)

        else:
            TotalPrice += price
    return TotalPrice

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    TotalGold1 = 0

    for person in range(len(people)):
        TotalGold1 = platinum2gold(person['cash']['platinum'])
        TotalGold2 =+ TotalGold1
        TotalGold1 = silver2gold(person['cash']['silver'])
        TotalGold2 =+ TotalGold1
        TotalGold1 = copper2gold(person['cash']['copper'])
        TotalGold2 =+ TotalGold1
        
        TotalGold1 += person['cash']['gold']
    return round(TotalGold2,2)
        
    # PriceType = people[nummer]['cash'] 
    # for nummer in range(len(people)):
    #     if PriceType == 'platinum':
    #         TotalGold += platinum2gold('platinum')

##################### M04.D02.O9 ##################### 

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

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