def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # haal de juiste inhoud op
    adventuringFriends = []
    interestingInvestors = []
    adventuringInvestors = []
    investorsCuts = []
    goldCut = 0.0

    # verdeel de uitkomsten
    for person in people:
        #code aanvullen

        earnings.append({
            'name'   : '??',
            'start'  : 0.0,
            'end'    : 0.0
        })

    return earnings


# def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
#     # haal de juiste inhoud op
#     adventuringFriends = getAdventuringFriends(friends)
#     interestingInvestors = getInterestingInvestors(investors)
#     adventuringInvestors = getAdventuringInvestors(investors)
    
#     #variable 
#     aftrek_goud = 0
#     goudToAvonturier = 0.0
#     fellowship = [mainCharacter] + friends + investors 
#     fellowship_adventurCut = [mainCharacter] + adventuringFriends + adventuringInvestors
#     earnings = []

#     # verdeel de uitkomsten
#     adventurCut = (profitGold - sum(getInvestorsCuts(profitGold,investors)) ) / len(fellowship_adventurCut)
#     goudToAvonturier = len(adventuringFriends) * 10

#     for index in range (len(fellowship)):
#         startCash = round(getPersonCashInGold(fellowship[index]['cash']),2)
#         endCash = startCash
#         if fellowship[index] in [mainCharacter]:
#             endCash += goudToAvonturier + adventurCut
#         elif fellowship[index] in investors:
#             if fellowship[index] in interestingInvestors and fellowship[index] in adventuringInvestors :
#                 investorsGoud = round(profitGold / 100 * fellowship[index][ 'profitReturn'],2)
#                 endCash += investorsGoud + adventurCut
#             elif fellowship[index] in interestingInvestors:
#                 investorsGoud = round(profitGold / 100 * fellowship[index][ 'profitReturn'],2)
#                 endCash += investorsGoud
#         elif fellowship[index] in friends:
#             if fellowship[index] in adventuringFriends:
#                 endCash += (adventurCut - 10)
#         earnings.append({
#                 'name'   : fellowship[index]['name'],
#                 'start'  : round(startCash,2),
#                 'end'    : round(endCash,2)
#             })
#     return earnings



